from telegram import Update
from telegram.ext import ContextTypes
from .scope import normalize_host, require_in_scope
from .reports import markdown_report
from .llm import ask

class Handlers:
    def __init__(self, db, settings): self.db, self.settings = db, settings
    async def auth(self, update):
        ids=self.settings.allowed_user_ids
        return not ids or update.effective_user.id in ids
    async def start(self, u: Update, c: ContextTypes.DEFAULT_TYPE):
        if not await self.auth(u): return
        await u.message.reply_text("BugBounty Gateway is ready. Use /help for commands.")
    async def help(self, u, c):
        if not await self.auth(u): return
        await u.message.reply_text("/target add host | program\n/target list\n/target remove host\n/finding add host | title | severity | details\n/finding list\n/report ID\n/ask question\n/status")
    async def status(self,u,c):
        if not await self.auth(u): return
        await u.message.reply_text(f"Targets: {len(self.db.targets())}\nFindings: {len(self.db.findings())}\nLLM: {'configured' if self.settings.llm_base_url and self.settings.llm_model else 'not configured'}")
    async def target(self,u,c):
        if not await self.auth(u): return
        text=" ".join(c.args)
        try:
            if text.startswith("add "):
                host,program=[x.strip() for x in text[4:].split("|",1)]; self.db.add_target(normalize_host(host),program); await u.message.reply_text("Target added to local scope.")
            elif text=="list": await u.message.reply_text("\n".join(f"{t.host} — {t.program}" for t in self.db.targets()) or "No targets.")
            elif text.startswith("remove "): self.db.remove_target(normalize_host(text[7:])); await u.message.reply_text("Target removed.")
            else: await self.help(u,c)
        except Exception as e: await u.message.reply_text(f"Error: {e}")
    async def finding(self,u,c):
        if not await self.auth(u): return
        text=" ".join(c.args)
        try:
            if text.startswith("add "):
                host,title,severity,details=[x.strip() for x in text[4:].split("|",3)]; host=require_in_scope(self.db,host); fid=self.db.add_finding(host,title,severity,details); await u.message.reply_text(f"Finding #{fid} saved.")
            elif text=="list": await u.message.reply_text("\n".join(f"#{f.id} [{f.severity}] {f.target} — {f.title}" for f in self.db.findings()) or "No findings.")
            else: await self.help(u,c)
        except Exception as e: await u.message.reply_text(f"Error: {e}")
    async def report(self,u,c):
        if not await self.auth(u): return
        try:
            f=self.db.finding(int(c.args[0])); await u.message.reply_text(markdown_report(f) if f else "Finding not found.")
        except Exception as e: await u.message.reply_text(f"Error: {e}")
    async def ask(self,u,c):
        if not await self.auth(u): return
        try: await u.message.reply_text(await ask(self.settings.llm_base_url,self.settings.llm_api_key,self.settings.llm_model," ".join(c.args)))
        except Exception as e: await u.message.reply_text(f"LLM error: {e}")

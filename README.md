# Hermes Agent

هذا المستودع لا يحتوي على نسخة معدّلة أو مشروعًا مشابهًا. مجلد `hermes-agent` هو **Hermes Agent الرسمي نفسه** كمستودع Git submodule، ومثبت على commit محدد من upstream.

## تشغيل النسخة الرسمية

```bash
git clone --recurse-submodules https://github.com/komando48k-lgtm/bugbounty-telegram-gateway.git
cd bugbounty-telegram-gateway/hermes-agent
```

ثم استخدم تعليمات Hermes الرسمية، مثل:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc
hermes --version
```

ولبوابة المراسلة:

```bash
hermes gateway setup
hermes gateway start
```

**مهم:** لا توجد طبقة كود إضافية من هذا المشروع فوق Hermes. أي تحديثات أو سلوكيات جديدة تأتي من upstream الرسمي فقط.

Upstream: https://github.com/NousResearch/hermes-agent
Pinned upstream commit: `b7ac3ba1cdf89f94dfe86de27e01358b194f4053`

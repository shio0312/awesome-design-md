<a href="https://github.com/VoltAgent/voltagent">
     <img width="1500" height="801" alt="claude-skills" src="https://github.com/user-attachments/assets/d012a0d2-cec3-4630-ba5e-acc339dbe6cf" />
</a>


<br/>
<br/>

<div align="center">
    <strong>Curated collection of DESIGN.md files inspired by developer focused websites.</strong>
    <br />
    <br />

</div>

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![DESIGN.md Count](https://img.shields.io/badge/DESIGN.md%20count-298-10b981?style=classic)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-design-md?label=Last%20update&style=classic)](https://github.com/VoltAgent/awesome-design-md)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)

</div>
</div>

# Awesome DESIGN.md

Copy a DESIGN.md into your project, tell your AI agent "build me a page that looks like this" and get pixel-perfect UI that actually matches.


## What is DESIGN.md?

[DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/) is a new concept introduced by Google Stitch. A plain-text design system document that AI agents read to generate consistent UI.

It's just a markdown file. No Figma exports, no JSON schemas, no special tooling. Drop it into your project root and any AI coding agent or Google Stitch instantly understands how your UI should look. Markdown is the format LLMs read best, so there's nothing to parse or configure.

| File | Who reads it | What it defines |
|------|-------------|-----------------|
| `AGENTS.md` | Coding agents | How to build the project |
| `DESIGN.md` | Design agents | How the project should look and feel |

**This repo provides ready-to-use DESIGN.md files** extracted from real websites. 



## What's Inside Each DESIGN.md

Every file follows the [Stitch DESIGN.md format](https://stitch.withgoogle.com/docs/design-md/format/) with extended sections:

| # | Section | What it captures |
|---|---------|-----------------|
| 1 | Visual Theme & Atmosphere | Mood, density, design philosophy |
| 2 | Color Palette & Roles | Semantic name + hex + functional role |
| 3 | Typography Rules | Font families, full hierarchy table |
| 4 | Component Stylings | Buttons, cards, inputs, navigation with states |
| 5 | Layout Principles | Spacing scale, grid, whitespace philosophy |
| 6 | Depth & Elevation | Shadow system, surface hierarchy |
| 7 | Do's and Don'ts | Design guardrails and anti-patterns |
| 8 | Responsive Behavior | Breakpoints, touch targets, collapsing strategy |
| 9 | Agent Prompt Guide | Quick color reference, ready-to-use prompts |

Each site includes:

| File | Purpose |
|------|---------|
| `DESIGN.md` | The design system (what agents read) |
| `preview.html` | Visual catalog showing color swatches, type scale, buttons, cards |
| `preview-dark.html` | Same catalog with dark surfaces |

### How to Use

#### Option 1: Use Existing DESIGN.md

1. Copy a site's `DESIGN.md` into your project root
2. Tell your AI agent to use it.

#### Option 2: Generate Your Own DESIGN.md 🆕

Use our **automated DESIGN.md generator** to create design system documentation for any website:

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Set up your Anthropic API key
cp .env.example .env
# Edit .env and add your API key

# Run the interactive generator
python suggest_design.py
```

The tool will:
- Fetch and analyze any website's design
- Extract colors, typography, components, and layout patterns
- Generate a complete DESIGN.md using Claude AI
- Save it to `design-md/[site-name]/DESIGN.md`
- Automatically add the site to `sites.yaml` for future updates

#### Option 3: Update Existing DESIGN.md 🆕

Keep your DESIGN.md files up-to-date when websites change their design:

**Manual update:**
```bash
python update_design.py
```

Select sites to update interactively, or update all sites at once.

**Automatic updates (GitHub Actions):**
- Weekly automated checks for design changes
- Auto-generates PRs when changes detected
- Set `ANTHROPIC_API_KEY` in GitHub Secrets
- Configure which sites to auto-update in `sites.yaml`

See [USAGE.md](USAGE.md) for detailed instructions.

#### Option 4: Sync from Refero Styles 🆕

Import ready-made design systems from [Refero Styles](https://styles.refero.design/) — a curated library of design tokens extracted from real websites. No API key required:

```bash
# Browse the catalog (✓ = already synced)
python sync_refero_styles.py --list

# Sync a specific style by URL or ID
python sync_refero_styles.py https://styles.refero.design/style/<id>

# Sync the whole catalog
python sync_refero_styles.py --all

# Re-sync everything previously imported
python sync_refero_styles.py --update
```

Synced styles are saved to `design-md/<site>/DESIGN.md`, registered in `sites.yaml` with `source: refero-styles`, and listed in the [Refero Styles](#refero-styles) section below. They are excluded from the Claude-based auto-update (`auto_update: false`) — use `--update` to refresh them from Refero instead.


## Request a DESIGN.md

[Open a GitHub issue with this template](https://github.com/VoltAgent/awesome-design-md/issues/new?template=design-md-request.yml) to request a DESIGN.md generation for a website.


## Collection

### AI & Machine Learning

- [**Claude**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/claude/) - Anthropic's AI assistant. Warm terracotta accent, clean editorial layout
- [**Cohere**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/cohere/) - Enterprise AI platform. Vibrant gradients, data-rich dashboard aesthetic
- [**ElevenLabs**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/elevenlabs/) - AI voice platform. Dark cinematic UI, audio-waveform aesthetics
- [**Minimax**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/minimax/) - AI model provider. Bold dark interface with neon accents
- [**Mistral AI**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mistral.ai/) - Open-weight LLM provider. French-engineered minimalism, purple-toned
- [**Ollama**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/ollama/) - Run LLMs locally. Terminal-first, monochrome simplicity
- [**OpenCode AI**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/opencode.ai/) - AI coding platform. Developer-centric dark theme
- [**Replicate**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/replicate/) - Run ML models via API. Clean white canvas, code-forward
- [**RunwayML**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/runwayml/) - AI video generation. Cinematic dark UI, media-rich layout
- [**Together AI**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/together.ai/) - Open-source AI infrastructure. Technical, blueprint-style design
- [**VoltAgent**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/voltagent/) - AI agent framework. Void-black canvas, emerald accent, terminal-native
- [**xAI**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/x.ai/) - Elon Musk's AI lab. Stark monochrome, futuristic minimalism

### Developer Tools & Platforms

- [**Cursor**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/cursor/) - AI-first code editor. Sleek dark interface, gradient accents
- [**Expo**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/expo/) - React Native platform. Dark theme, tight letter-spacing, code-centric
- [**Linear**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/linear.app/) - Project management for engineers. Ultra-minimal, precise, purple accent
- [**Lovable**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/lovable/) - AI full-stack builder. Playful gradients, friendly dev aesthetic
- [**Mintlify**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mintlify/) - Documentation platform. Clean, green-accented, reading-optimized
- [**PostHog**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/posthog/) - Product analytics. Playful hedgehog branding, developer-friendly dark UI
- [**Raycast**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/raycast/) - Productivity launcher. Sleek dark chrome, vibrant gradient accents
- [**Resend**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/resend/) - Email API for developers. Minimal dark theme, monospace accents
- [**Sentry**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/sentry/) - Error monitoring. Dark dashboard, data-dense, pink-purple accent
- [**Supabase**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/supabase/) - Open-source Firebase alternative. Dark emerald theme, code-first
- [**Superhuman**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/superhuman/) - Fast email client. Premium dark UI, keyboard-first, purple glow
- [**Vercel**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/vercel/) - Frontend deployment platform. Black and white precision, Geist font
- [**Warp**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/warp/) - Modern terminal. Dark IDE-like interface, block-based command UI
- [**Zapier**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/zapier/) - Automation platform. Warm orange, friendly illustration-driven

### Infrastructure & Cloud

- [**ClickHouse**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/clickhouse/) - Fast analytics database. Yellow-accented, technical documentation style
- [**Composio**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/composio/) - Tool integration platform. Modern dark with colorful integration icons
- [**HashiCorp**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/hashicorp/) - Infrastructure automation. Enterprise-clean, black and white
- [**MongoDB**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/mongodb/) - Document database. Green leaf branding, developer documentation focus
- [**Sanity**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/sanity/) - Headless CMS. Red accent, content-first editorial layout
- [**Stripe**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/stripe/) - Payment infrastructure. Signature purple gradients, weight-300 elegance

### Design & Productivity

- [**Airtable**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/airtable/) - Spreadsheet-database hybrid. Colorful, friendly, structured data aesthetic
- [**Cal.com**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/cal/) - Open-source scheduling. Clean neutral UI, developer-oriented simplicity
- [**Clay**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/clay/) - Creative agency. Organic shapes, soft gradients, art-directed layout
- [**Figma**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/figma/) - Collaborative design tool. Vibrant multi-color, playful yet professional
- [**Framer**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/framer/) - Website builder. Bold black and blue, motion-first, design-forward
- [**Intercom**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/intercom/) - Customer messaging. Friendly blue palette, conversational UI patterns
- [**Miro**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/miro/) - Visual collaboration. Bright yellow accent, infinite canvas aesthetic
- [**Notion**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/notion/) - All-in-one workspace. Warm minimalism, serif headings, soft surfaces
- [**Pinterest**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/pinterest/) - Visual discovery platform. Red accent, masonry grid, image-first
- [**Webflow**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/webflow/) - Visual web builder. Blue-accented, polished marketing site aesthetic

### Fintech & Crypto

- [**Coinbase**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/coinbase/) - Crypto exchange. Clean blue identity, trust-focused, institutional feel
- [**Kraken**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/kraken/) - Crypto trading platform. Purple-accented dark UI, data-dense dashboards
- [**Revolut**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/revolut/) - Digital banking. Sleek dark interface, gradient cards, fintech precision
- [**Wise**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/wise/) - International money transfer. Bright green accent, friendly and clear

### Enterprise & Consumer

- [**Airbnb**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/airbnb/) - Travel marketplace. Warm coral accent, photography-driven, rounded UI
- [**Apple**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/apple/) - Consumer electronics. Premium white space, SF Pro, cinematic imagery
- [**IBM**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/ibm/) - Enterprise technology. Carbon design system, structured blue palette
- [**NVIDIA**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/nvidia/) - GPU computing. Green-black energy, technical power aesthetic
- [**SpaceX**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/spacex/) - Space technology. Stark black and white, full-bleed imagery, futuristic
- [**Spotify**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/spotify/) - Music streaming. Vibrant green on dark, bold type, album-art-driven
- [**Uber**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/uber/) - Mobility platform. Bold black and white, tight type, urban energy

### Car Brands

- [**BMW**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/bmw/) - Luxury automotive. Dark premium surfaces, precise German engineering aesthetic
- [**Ferrari**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/ferrari/) - Luxury automotive. Chiaroscuro black-white editorial, Ferrari Red with extreme sparseness
- [**Lamborghini**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/lamborghini/) - Luxury automotive. True black cathedral, gold accent, LamboType custom Neo-Grotesk
- [**Renault**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/renault/) - French automotive. Vivid aurora gradients, NouvelR proprietary typeface, zero-radius buttons
- [**Tesla**](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/tesla/) - Electric vehicles. Radical subtraction, cinematic full-viewport photography, Universal Sans

### Japanese Design Systems

- [**ABEMA**](design-md/abema/) - 動画配信サービス。ダーク基調の没入感ある映像コンテンツUI
- [**Ameba Spindle**](design-md/ameba-spindle/) - CyberAgent Ameba's design system. Friendly media UI, warm approachable aesthetic
- [**connpass**](design-md/connpass/) - IT勉強会・イベント管理プラットフォーム。シンプルな開発者向けUI
- [**Cookpad**](design-md/cookpad/) - レシピ投稿・検索サービス。温かみのある食欲をそそるUI
- [**Cybozu**](design-md/cybozu/) - グループウェア・SaaS企業コーポレートサイト。企業理念を前面に出したUI
- [**Digital Agency (DADS)**](design-md/digital-agency/) - Japan Digital Agency design system. Accessible, structured government UI
- [**Digital Agency Japan**](design-md/digital-go/) - デジタル庁公式サイト。行政サービスのデジタル化を推進するUI
- [**Droga5 Japan**](design-md/droga5/) - クリエイティブエージェンシー。大胆でアーティスティックなUI
- [**freee**](design-md/freee/) - クラウド会計・人事労務SaaS。Vibes Design System採用の業務系UI
- [**Goodpatch Sparkle**](design-md/goodpatch-sparkle/) - Goodpatch's design system. Refined and polished, design-agency quality
- [**Hoshino Resorts**](design-md/hoshinoresorts/) - 星野リゾート。和の美意識を取り入れた高級感あるUI
- [**LINE**](design-md/line/) - メッセージアプリ。グリーンブランドカラーのフレンドリーなUI
- [**Mitsubishi Estate**](design-md/mec/) - 三菱地所コーポレートサイト。重厚感と信頼性を持つ不動産大手UI
- [**メルカリ**](design-md/mercari/) - フリマアプリ最大手。赤いブランドカラーのC2Cマーケットプレイス向けUI
- [**マネーフォワード**](design-md/moneyforward/) - 家計簿・資産管理・会計SaaS。信頼感を演出するフィンテックUI
- [**MOSH**](design-md/mosh/) - クリエイター向けサービス販売。Tailwind CSS v4採用のモダンなUI
- [**無印良品**](design-md/muji/) - MUJIネットストア。ミニマリズムを体現した余白重視のシンプルなUI
- [**日本経済新聞**](design-md/nikkei/) - 日経電子版。情報密度の高いニュースメディアUI
- [**Nintendo Japan**](design-md/nintendo/) - 任天堂日本公式サイト。遊び心あるカラフルなゲームブランドUI
- [**note**](design-md/note/) - コンテンツプラットフォーム。Tailwind + Svelte採用のクリエイター向けUI
- [**Novasell**](design-md/novasell/) - ラクスルグループのAIマーケティングエージェンシー。モダンなB2B SaaS UI
- [**PayPay**](design-md/paypay/) - QRコード決済。赤×黄のビビッドなブランドカラーが特徴
- [**Pepabo Design**](design-md/pepabo/) - GMO Pepabo's design guidelines. Friendly, creator-focused aesthetic
- [**pixiv**](design-md/pixiv/) - イラスト・マンガのSNS。クリエイター作品を引き立てるダーク対応UI
- [**Qiita**](design-md/qiita/) - 技術記事投稿プラットフォーム。開発者向けコードブロック重視UI
- [**楽天市場**](design-md/rakuten/) - 国内最大のECモール。情報密度が高い楽天レッドのにぎやかなUI
- [**Raksul Kamii**](design-md/raksul-kamii/) - Raksul's design system. Clean business UI for print and logistics services
- [**Sansan**](design-md/sansan/) - 名刺管理・営業DX SaaS。洗練されたビジネス向けUI
- [**Sansan One Design**](design-md/sansan-one-design/) - Sansan's One Design System. Clean and functional enterprise UI
- [**Serendie**](design-md/serendie/) - Sony's design system. Global-quality, precision-engineered components
- [**SmartHR Design**](design-md/smarthr/) - SmartHR's design system. Simple and functional HR SaaS UI
- [**SPEEDA Falcon**](design-md/speeda/) - UZABASE's B2B economic intelligence platform. Precise, data-dense, global-ready UI
- [**STUDIO**](design-md/studio/) - ノーコードウェブ制作ツール。クリエイティブでビジュアル重視のUI
- [**食べログ**](design-md/tabelog/) - グルメ情報・レストラン予約。食欲をそそる温かみのある情報密度高めUI
- [**トヨタ**](design-md/toyota/) - トヨタ自動車日本公式サイト。128件のCSSカスタムプロパティを持つ独自トークン体系
- [**Ubie Vitals**](design-md/ubie-vitals/) - Ubie's design system. Trustworthy medical-grade UI, accessible and calm
- [**UNIQLO Japan**](design-md/uniqlo/) - ユニクロ日本公式ECサイト。シンプルでコンテンツファーストなファッションUI
- [**Wantedly**](design-md/wantedly/) - Wantedly's UI components. Professional yet approachable, Japanese business SNS aesthetic
- [**WIRED Japan**](design-md/wired/) - テクノロジー・カルチャーメディア。styled-componentsベースのエディトリアルUI
- [**Zenn**](design-md/zenn/) - 技術記事・本プラットフォーム。Zennブルー(#3ea8ff)が特徴のデベロッパー向けUI

<!-- refero-styles:start -->
### Refero Styles

Design systems synced from [Refero Styles](https://styles.refero.design) via `sync_refero_styles.py`.

- [**099 SUPPLY**](design-md/099-supply/) - Design system synced from Refero Styles
- [**14islands**](design-md/14islands/) - Design system synced from Refero Styles
- [**70Materia**](design-md/70materia/) - Design system synced from Refero Styles
- [**Active Theory**](design-md/active-theory/) - Design system synced from Refero Styles
- [**Agence Foudre**](design-md/agence-foudre/) - Design system synced from Refero Styles
- [**AgentQL**](design-md/agentql/) - Design system synced from Refero Styles
- [**AI for Business**](design-md/ai-for-business/) - Design system synced from Refero Styles
- [**Air**](design-md/air/) - Design system synced from Refero Styles
- [**Airbnb**](design-md/airbnb-refero/) - Design system synced from Refero Styles
- [**Altitude**](design-md/altitude/) - Design system synced from Refero Styles
- [**amp**](design-md/amp/) - Design system synced from Refero Styles
- [**Amrit Palace**](design-md/amrit-palace/) - Design system synced from Refero Styles
- [**Analogue**](design-md/analogue/) - Design system synced from Refero Styles
- [**Anthropic**](design-md/anthropic/) - Design system synced from Refero Styles
- [**Antimetal**](design-md/antimetal/) - Design system synced from Refero Styles
- [**Apple**](design-md/apple-refero/) - Design system synced from Refero Styles
- [**Apple (España)**](design-md/apple-espa-a/) - Design system synced from Refero Styles
- [**Apple (España)**](design-md/apple-espa-a-refero/) - Design system synced from Refero Styles
- [**Apple (España)**](design-md/apple-espa-a-refero-a4f123f2/) - Design system synced from Refero Styles
- [**Arcade**](design-md/arcade/) - Design system synced from Refero Styles
- [**Arsenijs Fabrica**](design-md/arsenijs-fabrica/) - Design system synced from Refero Styles
- [**Arva**](design-md/arva/) - Design system synced from Refero Styles
- [**Attio**](design-md/attio/) - Design system synced from Refero Styles
- [**Augen Pro**](design-md/augen-pro/) - Design system synced from Refero Styles
- [**August Health EHR**](design-md/august-health-ehr/) - Design system synced from Refero Styles
- [**Auros**](design-md/auros/) - Design system synced from Refero Styles
- [**Authkit**](design-md/authkit/) - Design system synced from Refero Styles
- [**Awesomic**](design-md/awesomic/) - Design system synced from Refero Styles
- [**Axiom**](design-md/axiom/) - Design system synced from Refero Styles
- [**Backlight**](design-md/backlight/) - Design system synced from Refero Styles
- [**BelArosa Chalet**](design-md/belarosa-chalet/) - Design system synced from Refero Styles
- [**bella Kitchen Appliances**](design-md/bella-kitchen-appliances/) - Design system synced from Refero Styles
- [**Branding**](design-md/branding/) - Design system synced from Refero Styles
- [**Brex**](design-md/brex/) - Design system synced from Refero Styles
- [**Cal.com**](design-md/cal-com/) - Design system synced from Refero Styles
- [**Caldera**](design-md/caldera/) - Design system synced from Refero Styles
- [**Calendly.com**](design-md/calendly-com/) - Design system synced from Refero Styles
- [**Changelog**](design-md/changelog/) - Design system synced from Refero Styles
- [**ChatGPT**](design-md/chatgpt/) - Design system synced from Refero Styles
- [**Ciridae**](design-md/ciridae/) - Design system synced from Refero Styles
- [**Claude**](design-md/claude-refero/) - Design system synced from Refero Styles
- [**Clearbit**](design-md/clearbit/) - Design system synced from Refero Styles
- [**Clerk**](design-md/clerk/) - Design system synced from Refero Styles
- [**ClickUp™**](design-md/clickup/) - Design system synced from Refero Styles
- [**Compound**](design-md/compound/) - Design system synced from Refero Styles
- [**Convex**](design-md/convex/) - Design system synced from Refero Styles
- [**Cosmos**](design-md/cosmos/) - Design system synced from Refero Styles
- [**Cursor**](design-md/cursor-refero/) - Design system synced from Refero Styles
- [**Custo**](design-md/custo/) - Design system synced from Refero Styles
- [**Customer.io**](design-md/customer-io/) - Design system synced from Refero Styles
- [**Dash Digital Studio**](design-md/dash-digital-studio/) - Design system synced from Refero Styles
- [**Default**](design-md/default/) - Design system synced from Refero Styles
- [**Dennis Snellenberg**](design-md/dennis-snellenberg/) - Design system synced from Refero Styles
- [**Depot**](design-md/depot/) - Design system synced from Refero Styles
- [**Dimension**](design-md/dimension/) - Design system synced from Refero Styles
- [**Discord**](design-md/discord/) - Design system synced from Refero Styles
- [**Ditto**](design-md/ditto/) - Design system synced from Refero Styles
- [**Dock**](design-md/dock/) - Design system synced from Refero Styles
- [**dope.security**](design-md/dope-security/) - Design system synced from Refero Styles
- [**Doppler**](design-md/doppler/) - Design system synced from Refero Styles
- [**Dovetail**](design-md/dovetail/) - Design system synced from Refero Styles
- [**Dovetail**](design-md/dovetail-refero/) - Design system synced from Refero Styles
- [**Dub**](design-md/dub/) - Design system synced from Refero Styles
- [**Duolingo**](design-md/duolingo/) - Design system synced from Refero Styles
- [**Duolingo**](design-md/duolingo-refero/) - Design system synced from Refero Styles
- [**Dyotanya**](design-md/dyotanya/) - Design system synced from Refero Styles
- [**Ease Health**](design-md/ease-health/) - Design system synced from Refero Styles
- [**Eindhoven Design District**](design-md/eindhoven-design-district/) - Design system synced from Refero Styles
- [**ElevenLabs**](design-md/elevenlabs-refero/) - Design system synced from Refero Styles
- [**Factory**](design-md/factory/) - Design system synced from Refero Styles
- [**Family**](design-md/family/) - Design system synced from Refero Styles
- [**Fey**](design-md/fey/) - Design system synced from Refero Styles
- [**Flighty**](design-md/flighty/) - Design system synced from Refero Styles
- [**Flowmapp**](design-md/flowmapp/) - Design system synced from Refero Styles
- [**Flying Papers**](design-md/flying-papers/) - Design system synced from Refero Styles
- [**Foodnoms**](design-md/foodnoms/) - Design system synced from Refero Styles
- [**Frame.io**](design-md/frame-io/) - Design system synced from Refero Styles
- [**Framer**](design-md/framer-refero/) - Design system synced from Refero Styles
- [**General Intelligence Company**](design-md/general-intelligence-company/) - Design system synced from Refero Styles
- [**Geniestudio**](design-md/geniestudio/) - Design system synced from Refero Styles
- [**Getharvest**](design-md/getharvest/) - Design system synced from Refero Styles
- [**Ghia**](design-md/ghia/) - Design system synced from Refero Styles
- [**GitHub**](design-md/github/) - Design system synced from Refero Styles
- [**Gleap**](design-md/gleap/) - Design system synced from Refero Styles
- [**Grafik**](design-md/grafik/) - Design system synced from Refero Styles
- [**Grove AI**](design-md/grove-ai/) - Design system synced from Refero Styles
- [**Gsap**](design-md/gsap/) - Design system synced from Refero Styles
- [**Handsome Frank**](design-md/handsome-frank/) - Design system synced from Refero Styles
- [**Harness.io**](design-md/harness-io/) - Design system synced from Refero Styles
- [**Henry**](design-md/henry/) - Design system synced from Refero Styles
- [**Home**](design-md/home/) - Design system synced from Refero Styles
- [**Huly**](design-md/huly/) - Design system synced from Refero Styles
- [**Hungry Tiger**](design-md/hungry-tiger/) - Design system synced from Refero Styles
- [**Hyer Aviation**](design-md/hyer-aviation/) - Design system synced from Refero Styles
- [**Hyperstudio**](design-md/hyperstudio/) - Design system synced from Refero Styles
- [**Idle Finance**](design-md/idle-finance/) - Design system synced from Refero Styles
- [**Index**](design-md/index/) - Design system synced from Refero Styles
- [**Integrated Biosciences**](design-md/integrated-biosciences/) - Design system synced from Refero Styles
- [**Intercom**](design-md/intercom-refero/) - Design system synced from Refero Styles
- [**INVERSA**](design-md/inversa/) - Design system synced from Refero Styles
- [**Karl**](design-md/karl/) - Design system synced from Refero Styles
- [**Ko-fi**](design-md/ko-fi/) - Design system synced from Refero Styles
- [**Lamborghini.com**](design-md/lamborghini-com/) - Design system synced from Refero Styles
- [**LaunchDarkly**](design-md/launchdarkly/) - Design system synced from Refero Styles
- [**Legora**](design-md/legora/) - Design system synced from Refero Styles
- [**Letter**](design-md/letter/) - Design system synced from Refero Styles
- [**Letters**](design-md/letters/) - Design system synced from Refero Styles
- [**Lightdash**](design-md/lightdash/) - Design system synced from Refero Styles
- [**Linear**](design-md/linear/) - Design system synced from Refero Styles
- [**Lpalo**](design-md/lpalo/) - Design system synced from Refero Styles
- [**Mercury**](design-md/mercury/) - Design system synced from Refero Styles
- [**Metalab**](design-md/metalab/) - Design system synced from Refero Styles
- [**Micro**](design-md/micro/) - Design system synced from Refero Styles
- [**Midday**](design-md/midday/) - Design system synced from Refero Styles
- [**Midjourney**](design-md/midjourney/) - Design system synced from Refero Styles
- [**MindMarket**](design-md/mindmarket/) - Design system synced from Refero Styles
- [**Mintlify**](design-md/mintlify-refero/) - Design system synced from Refero Styles
- [**Miranda**](design-md/miranda/) - Design system synced from Refero Styles
- [**Mobbin**](design-md/mobbin/) - Design system synced from Refero Styles
- [**Modal**](design-md/modal/) - Design system synced from Refero Styles
- [**Monad**](design-md/monad/) - Design system synced from Refero Styles
- [**monday.com**](design-md/monday-com/) - Design system synced from Refero Styles
- [**mono**](design-md/mono/) - Design system synced from Refero Styles
- [**Monocle**](design-md/monocle/) - Design system synced from Refero Styles
- [**monopo saigon**](design-md/monopo-saigon/) - Design system synced from Refero Styles
- [**Munro Partners**](design-md/munro-partners/) - Design system synced from Refero Styles
- [**NCDA**](design-md/ncda/) - Design system synced from Refero Styles
- [**Notion**](design-md/notion-refero/) - Design system synced from Refero Styles
- [**OFF+BRAND.**](design-md/off-brand/) - Design system synced from Refero Styles
- [**OFFFICE :**](design-md/offfice/) - Design system synced from Refero Styles
- [**Officevibe**](design-md/officevibe/) - Design system synced from Refero Styles
- [**OLIPOP**](design-md/olipop/) - Design system synced from Refero Styles
- [**ON.energy**](design-md/on-energy/) - Design system synced from Refero Styles
- [**OpenAI**](design-md/openai/) - Design system synced from Refero Styles
- [**Operate**](design-md/operate/) - Design system synced from Refero Styles
- [**Orderful**](design-md/orderful/) - Design system synced from Refero Styles
- [**Origin Financial**](design-md/origin-financial/) - Design system synced from Refero Styles
- [**ORYZO AI**](design-md/oryzo-ai/) - Design system synced from Refero Styles
- [**Outsource Consultants**](design-md/outsource-consultants/) - Design system synced from Refero Styles
- [**Oxide Computer Company**](design-md/oxide-computer-company/) - Design system synced from Refero Styles
- [**Pa'lais**](design-md/pa-lais/) - Design system synced from Refero Styles
- [**Passionfroot**](design-md/passionfroot/) - Design system synced from Refero Styles
- [**Peak Design**](design-md/peak-design/) - Design system synced from Refero Styles
- [**Perk**](design-md/perk/) - Design system synced from Refero Styles
- [**Pirsch Analytics**](design-md/pirsch-analytics/) - Design system synced from Refero Styles
- [**Playful**](design-md/playful/) - Design system synced from Refero Styles
- [**Portal**](design-md/portal/) - Design system synced from Refero Styles
- [**Portrait**](design-md/portrait/) - Design system synced from Refero Styles
- [**Programa**](design-md/programa/) - Design system synced from Refero Styles
- [**Raus**](design-md/raus/) - Design system synced from Refero Styles
- [**Raw Materials**](design-md/raw-materials/) - Design system synced from Refero Styles
- [**Raycast**](design-md/raycast-refero/) - Design system synced from Refero Styles
- [**Reflect Notes**](design-md/reflect-notes/) - Design system synced from Refero Styles
- [**Relate**](design-md/relate/) - Design system synced from Refero Styles
- [**Render**](design-md/render/) - Design system synced from Refero Styles
- [**Resend**](design-md/resend-refero/) - Design system synced from Refero Styles
- [**Revolut**](design-md/revolut-refero/) - Design system synced from Refero Styles
- [**Sauce Labs**](design-md/sauce-labs/) - Design system synced from Refero Styles
- [**Savee**](design-md/savee/) - Design system synced from Refero Styles
- [**Say Briefly**](design-md/say-briefly/) - Design system synced from Refero Styles
- [**Scheduling**](design-md/scheduling/) - Design system synced from Refero Styles
- [**Seed**](design-md/seed/) - Design system synced from Refero Styles
- [**Seline Analytics**](design-md/seline-analytics/) - Design system synced from Refero Styles
- [**Sequel**](design-md/sequel/) - Design system synced from Refero Styles
- [**Shares**](design-md/shares/) - Design system synced from Refero Styles
- [**Shop**](design-md/shop/) - Design system synced from Refero Styles
- [**Slack**](design-md/slack/) - Design system synced from Refero Styles
- [**Slash**](design-md/slash/) - Design system synced from Refero Styles
- [**Slush**](design-md/slush/) - Design system synced from Refero Styles
- [**Spotify**](design-md/spotify-refero/) - Design system synced from Refero Styles
- [**Sprout Social**](design-md/sprout-social/) - Design system synced from Refero Styles
- [**Steep**](design-md/steep/) - Design system synced from Refero Styles
- [**Stripe**](design-md/stripe-refero/) - Design system synced from Refero Styles
- [**Structured**](design-md/structured/) - Design system synced from Refero Styles
- [**Subframe**](design-md/subframe/) - Design system synced from Refero Styles
- [**Supabase**](design-md/supabase-refero/) - Design system synced from Refero Styles
- [**Superhuman**](design-md/superhuman-refero/) - Design system synced from Refero Styles
- [**Superlist**](design-md/superlist/) - Design system synced from Refero Styles
- [**Superpower**](design-md/superpower/) - Design system synced from Refero Styles
- [**Superr**](design-md/superr/) - Design system synced from Refero Styles
- [**Tracky**](design-md/tracky/) - Design system synced from Refero Styles
- [**TWOMUCH.STUDIO**](design-md/twomuch-studio/) - Design system synced from Refero Styles
- [**Uber**](design-md/uber-refero/) - Design system synced from Refero Styles
- [**Ui**](design-md/ui/) - Design system synced from Refero Styles
- [**v0 by Vercel**](design-md/v0-by-vercel/) - Design system synced from Refero Styles
- [**Valo**](design-md/valo/) - Design system synced from Refero Styles
- [**VEED**](design-md/veed/) - Design system synced from Refero Styles
- [**Ventriloc**](design-md/ventriloc/) - Design system synced from Refero Styles
- [**Vercel**](design-md/vercel-refero/) - Design system synced from Refero Styles
- [**Visitors**](design-md/visitors/) - Design system synced from Refero Styles
- [**Vivid+Co**](design-md/vivid-co/) - Design system synced from Refero Styles
- [**Voiceflow**](design-md/voiceflow/) - Design system synced from Refero Styles
- [**Walden**](design-md/walden/) - Design system synced from Refero Styles
- [**Warp**](design-md/warp-refero/) - Design system synced from Refero Styles
- [**WHOOP**](design-md/whoop/) - Design system synced from Refero Styles
- [**Wise**](design-md/wise-refero/) - Design system synced from Refero Styles
- [**Wise Design**](design-md/wise-design/) - Design system synced from Refero Styles
- [**WRITER**](design-md/writer/) - Design system synced from Refero Styles
- [**xAI**](design-md/xai/) - Design system synced from Refero Styles
- [**Your workplace has the answer. Just ask Dala for it.**](design-md/your-workplace-has-the-answer-just-ask-dala-for-it/) - Design system synced from Refero Styles
<!-- refero-styles:end -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- **Improve existing files**: Fix wrong colors, missing tokens, weak descriptions
- **Report issues**: Let us know if something looks off

Before opening a PR, please [open an issue](https://github.com/VoltAgent/awesome-design-md/issues) first to discuss your idea and get feedback from maintainers.


## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of design system documents extracted from public websites. All DESIGN.md files are provided "as is" without warranty. The extracted design tokens represent publicly visible CSS values. We do not claim ownership of any site's visual identity. These documents exist to help AI agents generate consistent UI.

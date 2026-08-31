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

- [**099 SUPPLY**](design-md/099-supply/) - Gallery wall of black-on-white objects
- [**14islands**](design-md/14islands/) - Monochrome editorial gallery — A pristine gallery wall where oversized black typography and full-bleed photography ex...
- [**70Materia**](design-md/70materia/) - Architectural sample board on white paper — the UI is the mount, never the artwork.
- [**Active Theory**](design-md/active-theory/) - cosmic void with a single luminous portal — deep-space command deck where chrome whispers and the rendered world shouts
- [**Agence Foudre**](design-md/agence-foudre/) - Magazine splash page in lipstick pink.
- [**AgentQL**](design-md/agentql/) - Aurora glow over a midnight terminal
- [**AI for Business**](design-md/ai-for-business/) - Brutalist editorial showroom on warm gray
- [**Air**](design-md/air/) - midnight sky through glass sculpture
- [**Airbnb**](design-md/airbnb-refero/) - Quiet white gallery wall with one coral-red bookmark
- [**Altitude**](design-md/altitude/) - midnight financial editorial — a darkened trading floor printed on bone-white serif stock, lit only by thin borders a...
- [**amp**](design-md/amp/) - warm orange pill on cool white. The design feels like a premium fitness product photographed in a sunlit loft: one ob...
- [**Amrit Palace**](design-md/amrit-palace/) - spiced parchment gallery — a candlelit beige wall holding sparse saffron punctuation beneath breath-soft serif headli...
- [**Analogue**](design-md/analogue/) - Black gallery vitrine — products float in void
- [**Anthropic**](design-md/anthropic/) - scientific field journal on warm parchment — quiet ivory surfaces, editorial serif headlines, and a single clay accen...
- [**Antimetal**](design-md/antimetal/) - editorial observatory on cream paper — a quiet morning in a research journal where restraint signals confidence and t...
- [**Apple**](design-md/apple-refero/) - white room with a single blue switch.
- [**Apple (España)**](design-md/apple-espa-a/) - Cathedral of white space with whispered headlines. A vast pale hall where massive weight-700 type hangs in the air, t...
- [**Apple (España)**](design-md/apple-espa-a-refero/) - obsidian gallery vitrine — a dark showroom where a single titanium object glows against pure black
- [**Apple (España)**](design-md/apple-espa-a-refero-a4f123f2/) - Museum gallery in soft daylight — the gallery is a single, immersive, weightless white room where each product is spo...
- [**Arcade**](design-md/arcade/) - Electric blue ripple on white paper. A clean editorial canvas where a single vivid blue flows like liquid from corner...
- [**Arsenijs Fabrica**](design-md/arsenijs-fabrica/) - Editorial beauty spread under gallery lights. Pure-white gallery walls, a single warm strobe pulsing orange against t...
- [**Arva**](design-md/arva/) - Pastoral editorial magazine spread on a cream field
- [**Attio**](design-md/attio/) - Architectural editorial on white marble
- [**Augen Pro**](design-md/augen-pro/) - Apple keynote on surgical white — clinical, weightless, electric blue as single accent in monochrome void
- [**August Health EHR**](design-md/august-health-ehr/) - Warm cream pharmacy with violet ink — a humanist clinical surface that softens healthcare's typical sterility.
- [**Auros**](design-md/auros/) - Abyssal terminal with bioluminescent data orbs
- [**Authkit**](design-md/authkit/) - Frosted glass cathedral at midnight
- [**Awesomic**](design-md/awesomic/) - editorial zinc grid with confetti-orange punctuation.
- [**Axiom**](design-md/axiom/) - Terminal window at midnight — flat black canvas, monospaced text, and one orange cursor blinking
- [**Backlight**](design-md/backlight/) - Vermillion stamp on warm vellum — a printed catalog cover where one ink red commands the cream page and everything el...
- [**BelArosa Chalet**](design-md/belarosa-chalet/) - dusk on alpine vellum
- [**bella Kitchen Appliances**](design-md/bella-kitchen-appliances/) - Sunlit kitchen counter at golden hour — warm cream surfaces with a single pop of coral.
- [**Branding**](design-md/branding/) - Black gallery wall, blood-red punctuation — Oversized white display type floats on a void-like dark canvas, interrupt...
- [**Brex**](design-md/brex/) - White concrete, single ember — a clinical financial instrument where one orange spark does all the talking.
- [**Cal.com**](design-md/cal-com/) - Monochrome Utility, Human Touch. A system that prioritizes clarity and function with a stark black-and-white palette,...
- [**Caldera**](design-md/caldera/) - forge fire on warm limestone. The canvas is raw warm plaster, and every orange element reads as glowing embers presse...
- [**Calendly.com**](design-md/calendly-com/) - Navy ink on cool marble.
- [**Changelog**](design-md/changelog/) - observatory console behind dark glass.
- [**ChatGPT**](design-md/chatgpt/) - graphite ink on warm paper
- [**Ciridae**](design-md/ciridae/) - void chamber with ember pulse — a near-black cathedral where the only warm note is a thin line of ember rust, and eve...
- [**Claude**](design-md/claude-refero/) - Warm parchment printed artifact — ink on bone paper, clay as the only chromatic breath.
- [**Clearbit**](design-md/clearbit/) - data observatory on cloud paper — a room-bright, near-acromatic canvas where midnight ink and a single blue current d...
- [**Clerk**](design-md/clerk/) - Developer dashboard behind frosted violet glass — surfaces feel like a live IDE preview: dark product cards floating...
- [**ClickUp™**](design-md/clickup/) - Hardworking dashboard on white marble. The page is a product brochure for a productivity tool, so the visual language...
- [**Compound**](design-md/compound/) - ink-on-paper wealth journal — a quiet editorial system where one font at one weight does all the work, and the only c...
- [**Convex**](design-md/convex/) - Cream paper engineering notebook
- [**Cosmos**](design-md/cosmos/) - Linen gallery wall with floating polaroids
- [**Cursor**](design-md/cursor-refero/) - Warm parchment atelier lit by embers
- [**Custo**](design-md/custo/) - Gunmetal gallery with monolithic type. A muted gray-green showroom where a single dark object and 57px type do all th...
- [**Customer.io**](design-md/customer-io/) - dark spruce forest meeting cream paper
- [**Dash Digital Studio**](design-md/dash-digital-studio/) - Editorial museum on warm paper. A gallery where giant whisper-weight typography floats over off-white walls and full-...
- [**Default**](design-md/default/) - Mission control behind frosted glass — weight 400 headlines float over matte-black panels lit by thin blue ring-light...
- [**Dennis Snellenberg**](design-md/dennis-snellenberg/) - Dark editorial canvas with giant quiet headlines
- [**Depot**](design-md/depot/) - Dark server-rack terminal. A near-black developer console where one green LED signals action and the rest of the UI w...
- [**Dimension**](design-md/dimension/) - dusk-lit workspace with frosted glass panels
- [**Discord**](design-md/discord/) - Game world behind a chat bubble — every section is a self-contained environment with its own lighting and cast of cha...
- [**Ditto**](design-md/ditto/) - Sunlit wildflower compliance atelier. Warm cream surfaces, vivid yellow primary action, deep navy ink, organic color...
- [**Dock**](design-md/dock/) - Sunlit cream paper, cobalt pulse
- [**dope.security**](design-md/dope-security/) - Midnight terminal with violet beacons
- [**Doppler**](design-md/doppler/) - violet-lit vault at midnight. A near-black canvas glows with a single lavender signal and a green confirmation light,...
- [**Dovetail**](design-md/dovetail/) - blueprint control room at midnight.
- [**Dovetail**](design-md/dovetail-refero/) - Blueprint grid under a black moon — faint graph lines, white type, one violet spark.
- [**Dub**](design-md/dub/) - frosted link dashboard on rice paper
- [**Duolingo**](design-md/duolingo/) - Playful classroom mascot on white paper
- [**Duolingo**](design-md/duolingo-refero/) - Green playground with thick marker outlines
- [**Dyotanya**](design-md/dyotanya/) - Editorial sketchbook on warm paper — oversized serif confessions floating between hand-drawn squiggles
- [**Ease Health**](design-md/ease-health/) - Botanical greenhouse on cream paper
- [**Eindhoven Design District**](design-md/eindhoven-design-district/) - editorial brutalism on white paper — a municipal design manifesto rendered in oversized type, sparse photographs, and...
- [**ElevenLabs**](design-md/elevenlabs-refero/) - Warm cream editorial with whispered headlines. A Bauhaus studio notebook — eggshell paper, black ink, a single violet...
- [**Factory**](design-md/factory/) - Terminal war room at midnight. Factory is a stark black control surface where a single white card lands like a flashl...
- [**Family**](design-md/family/) - storybook spread on cream parchment
- [**Fey**](design-md/fey/) - Nocturnal Bloomberg terminal, matte-black with luminous type
- [**Flighty**](design-md/flighty/) - Control tower at midnight — a luminous control room with glowing screens floating around a single device
- [**Flowmapp**](design-md/flowmapp/) - White blueprint desk with one blue pen
- [**Flying Papers**](design-md/flying-papers/) - Saturday morning cartoon confessional
- [**Foodnoms**](design-md/foodnoms/) - Sunlit fruit market on white porcelain — warm orange, fresh green, and generous rounded forms
- [**Frame.io**](design-md/frame-io/) - Midnight cinema projection room.
- [**Framer**](design-md/framer-refero/) - neon gallery in the void
- [**General Intelligence Company**](design-md/general-intelligence-company/) - Literary journal beside a bonfire
- [**Geniestudio**](design-md/geniestudio/) - soft daylight notebook — the kind with generous margins and a single bold pen stroke
- [**Getharvest**](design-md/getharvest/) - Golden hour workbench — warm cream canvas, white floating cards, and one vivid orange flame.
- [**Ghia**](design-md/ghia/) - Mediterranean sunset on a vintage aperitivo label
- [**GitHub**](design-md/github/) - cosmic command deck with bioluminescent waypoints — a dark, atmospheric workspace where a single green glow marks the...
- [**Gleap**](design-md/gleap/) - warm cream-paper workspace with graphite accents — a studio where matte-black ink dots float over linen architecture.
- [**Grafik**](design-md/grafik/) - Editorial gallery on warm paper. A design annual laid out as a full-bleed screen — typographic grid lines, monochrome...
- [**Grove AI**](design-md/grove-ai/) - clinical journal in morning light — a single green word anchors a page of measured prose
- [**Gsap**](design-md/gsap/) - animated chalkboard in a design studio. A near-black wall, warm cream chalk, and five color-coded highlighters — one...
- [**Handsome Frank**](design-md/handsome-frank/) - Curator's atelier with living murals — a warm-paper gallery where illustrated worlds bloom against indigo frames.
- [**Harness.io**](design-md/harness-io/) - midnight mission control with phosphor-green accents
- [**Henry**](design-md/henry/) - Gothic broadside poster on warm cream paper. One hundred percent monochrome, no chromatic accent, all visual intensit...
- [**Home**](design-md/home/) - editorial broadsheet in a green room
- [**Huly**](design-md/huly/) - Aurora through a midnight observatory — the hero is a vertical beam of violet melting into coral, and every quiet sec...
- [**Hungry Tiger**](design-md/hungry-tiger/) - Turmeric-bright graffiti on a tandoor wall. A single gold-on-rust palette with display type so large it reads as a sp...
- [**Hyer Aviation**](design-md/hyer-aviation/) - Cockpit twilight over parchment. A pale dawn-sky meets a slab-serif logo the size of a fuselage, with one warm clay a...
- [**Hyperstudio**](design-md/hyperstudio/) - blueprint scratched into obsidian. Type and hairline borders carve white space from pure black, with the occasional g...
- [**Idle Finance**](design-md/idle-finance/) - Neon deep-sea trading floor — a dark navy terminal where a single cyan signal pierces the gloom.
- [**Index**](design-md/index/) - Blueprint on a backlit drafting table — the entire interface is a wireframe drawing, with one periwinkle annotation pen.
- [**Integrated Biosciences**](design-md/integrated-biosciences/) - bioluminescent laboratory at midnight
- [**Intercom**](design-md/intercom-refero/) - Warm cream editorial spread
- [**INVERSA**](design-md/inversa/) - topographic field terminal at midnight. A dark command surface where massive editorial type and a single neon-lime ma...
- [**Karl**](design-md/karl/) - Pop-up storybook diorama on a sunny afternoon
- [**Ko-fi**](design-md/ko-fi/) - Warm café chalkboard on cream paper.
- [**Lamborghini.com**](design-md/lamborghini-com/) - Showroom black with one yellow car under spotlights
- [**LaunchDarkly**](design-md/launchdarkly/) - Neon control room — a dark cockpit where violet signals pulse through charcoal panels.
- [**Legora**](design-md/legora/) - Editorial law journal on warm cream
- [**Letter**](design-md/letter/) - Private gallery with iridescent vault artifacts. A black-walled showroom where serif headlines float above chrome scu...
- [**Letters**](design-md/letters/) - morning clinic under open sky — a sterile white desk beneath a wash of soft blue, dotted with surgical-blue instruments.
- [**Lightdash**](design-md/lightdash/) - violet pixel-grid on drafting paper
- [**Linear**](design-md/linear/) - midnight precision instrument
- [**Lpalo**](design-md/lpalo/) - A children's storybook spread on warm peach paper — one slab-serif headline shouting through scattered crayon doodles.
- [**Mercury**](design-md/mercury/) - Alpine banking at blue hour
- [**Metalab**](design-md/metalab/) - black editorial spread — a serif headline breathing in void, annotated by a whisper-quiet grotesque
- [**Micro**](design-md/micro/) - sunrise over a digital meadow — a calm horizon gradient holding a quiet, ink-on-paper workspace beneath it.
- [**Midday**](design-md/midday/) - Editorial broadsheet on parchment — a 72px serif headline over warm stone, spaced sans-serif body text, pill-shaped c...
- [**Midjourney**](design-md/midjourney/) - Deep-ocean bioluminescent terminal. A pressurized darkness where intelligence visibly generates itself in ASCII strea...
- [**MindMarket**](design-md/mindmarket/) - Warm storybook on cream paper — a friendly editorial canvas where oversized Inter headlines and paper-cut characters...
- [**Mintlify**](design-md/mintlify-refero/) - Cloud garden over a glass desk. A hand-illustrated sky and a documentation product share the same frame — the only pl...
- [**Miranda**](design-md/miranda/) - Old-world broadsheet on warm cream — newspaper editorial for the digital age.
- [**Mobbin**](design-md/mobbin/) - Grayscale specimen board — a printer's proof sheet where typographic weight IS color.
- [**Modal**](design-md/modal/) - Phosphor terminal in a darkened server room — the vivid green is the only light source.
- [**Monad**](design-md/monad/) - editorial tech journal on warm parchment
- [**monday.com**](design-md/monday-com/) - white workshop with pastel sticky notes
- [**mono**](design-md/mono/) - White-walled gallery grid. A page organized like a museum contact sheet — stark white cells, thin black rules, and ty...
- [**Monocle**](design-md/monocle/) - Quality broadsheet on cream paper. A curated newsroom where every column earns its keep and the only color on the pag...
- [**monopo saigon**](design-md/monopo-saigon/) - Liquid iridescence behind editorial silence — a monochrome editorial gallery floating on molten light.
- [**Munro Partners**](design-md/munro-partners/) - Editorial parchment under alpine light — a warm cream canvas holding generous whitespace, a whisper-weight grotesque,...
- [**NCDA**](design-md/ncda/) - Architectural monograph in negative space. The NCDA wordmark at 62px is cropped by the viewport edge, turning a logo...
- [**Notion**](design-md/notion-refero/) - warm paper notebook under afternoon sun
- [**OFF+BRAND.**](design-md/off-brand/) - Iridescent sphere on warm parchment
- [**OFFFICE :**](design-md/offfice/) - noir gallery swallowed by monolithic type
- [**Officevibe**](design-md/officevibe/) - Editorial journal on warm cream paper. Think a thoughtful HR essay rendered as a product — serif italics whispering t...
- [**OLIPOP**](design-md/olipop/) - Retro apothecary cream and forest teal — a soda fountain menu printed on warm paper.
- [**ON.energy**](design-md/on-energy/) - High-voltage caution yellow on midnight steel
- [**OpenAI**](design-md/openai/) - Research lab notebook at noon.
- [**Operate**](design-md/operate/) - Botanist's data terminal
- [**Orderful**](design-md/orderful/) - industrial command deck — a logistics dispatcher's printed control sheet in black ink and surgical vermillion, every...
- [**Origin Financial**](design-md/origin-financial/) - midnight gallery of quiet wealth. A hushed, near-black room where oversized serif whispers and a few luminous color p...
- [**ORYZO AI**](design-md/oryzo-ai/) - Darkroom product editorial. A lone object floating in warm darkness, cream typography the only decoration.
- [**Outsource Consultants**](design-md/outsource-consultants/) - Architectural broadsheet on bone paper. A monograph aesthetic where one violent indigo section interrupts an otherwis...
- [**Oxide Computer Company**](design-md/oxide-computer-company/) - Datacenter rack at midnight with one green LED lit
- [**Pa'lais**](design-md/pa-lais/) - Botanical sketchbook dipped in honey. The cream paper canvas, blue toile-style line illustrations, and warm color blo...
- [**Passionfroot**](design-md/passionfroot/) - Twilight cloud library on warm parchment. A serif headline drifts above cream cards lit by a violet-to-coral sky, whe...
- [**Peak Design**](design-md/peak-design/) - Gallery wall, half lit
- [**Perk**](design-md/perk/) - electric lime on warm parchment paper
- [**Pirsch Analytics**](design-md/pirsch-analytics/) - sunlit paper notebook with highlighter swatches
- [**Playful**](design-md/playful/) - sunlit paper notebook with a hot-pink highlighter. A friendly, editorial product surface printed on warm cream stock,...
- [**Portal**](design-md/portal/) - twilight serif editorial — a premium indie magazine spread sitting inside a native iOS aesthetic
- [**Portrait**](design-md/portrait/) - polaroid memory wall on cream paper. A bright, off-white scrapbook where deep-navy ink provides the only text, the on...
- [**Programa**](design-md/programa/) - Swiss design studio at high noon. A white gallery wall lit by a single yellow desk lamp — everything is grayscale unt...
- [**Raus**](design-md/raus/) - Warm cabin journal on cream paper — every page a postcard from the woods.
- [**Raw Materials**](design-md/raw-materials/) - brutalist editorial on warm cream
- [**Raycast**](design-md/raycast-refero/) - Midnight command center, coral neon
- [**Reflect Notes**](design-md/reflect-notes/) - starlit violet cosmos — a dark observatory where notes float like constellations against a near-black indigo void.
- [**Relate**](design-md/relate/) - cool dawn over product canvas
- [**Render**](design-md/render/) - Blueprint on brushed aluminum. The interface reads as a clean, geometric engineering document — white space, hairline...
- [**Resend**](design-md/resend-refero/) - black velvet with violet neon
- [**Revolut**](design-md/revolut-refero/) - Monochrome editorial banking on cloud photography — white ink, pill buttons, one blue ribbon of color in an otherwise...
- [**Sauce Labs**](design-md/sauce-labs/) - Neon-lit command center on obsidian glass — a dark engineering console where a single green pulse marks every live si...
- [**Savee**](design-md/savee/) - Black canvas for visual curators
- [**Say Briefly**](design-md/say-briefly/) - creative agency sketchbook on cream paper
- [**Scheduling**](design-md/scheduling/) - Editorial ink on cream paper
- [**Seed**](design-md/seed/) - living organism under laboratory glass
- [**Seline Analytics**](design-md/seline-analytics/) - Quiet analyst's desk on warm paper
- [**Sequel**](design-md/sequel/) - Private screening after dark — a single warm lamp in an otherwise unlit cinema.
- [**Shares**](design-md/shares/) - Ivory terminal with violet pulse — a clinical white workspace where one color marks every deliberate action.
- [**Shop**](design-md/shop/) - Floating shopping constellation on white marble
- [**Slack**](design-md/slack/) - Aubergine stage with white spotlights. Deep plum dominates dark sections while a near-white canvas lets oversized Ava...
- [**Slash**](design-md/slash/) - Midnight vault with gilded ledger lines.
- [**Slush**](design-md/slush/) - inflatable sticker universe on pastel paper
- [**Spotify**](design-md/spotify-refero/) - Darkened record store at midnight — every surface recedes so the album art can glow.
- [**Sprout Social**](design-md/sprout-social/) - Green sprout on black slate. One vivid accent on a stark monochrome canvas, the color rationed to actions only, with...
- [**Steep**](design-md/steep/) - serif analytics on warm paper
- [**Stripe**](design-md/stripe-refero/) - indigo-ink ledger on frosted glass
- [**Structured**](design-md/structured/) - Renaissance gallery on putty paper
- [**Subframe**](design-md/subframe/) - graphite blueprint on warm vellum. A designer's drafting paper where every mark is either graphite or erasure, never...
- [**Supabase**](design-md/supabase-refero/) - Midnight code editor with phosphor green caret — a single chromatic pulse on a sea of charcoal.
- [**Superhuman**](design-md/superhuman-refero/) - golden hour editorial dashboard
- [**Superlist**](design-md/superlist/) - midnight workspace with coral embers — a quiet aubergine app surface where one warm orange spark signals every action
- [**Superpower**](design-md/superpower/) - Bioluminescent health command center
- [**Superr**](design-md/superr/) - Warm schoolyard notebook in soft afternoon light. A cream page, an orange marker uncapped, and a stack of sticker-lam...
- [**Tracky**](design-md/tracky/) - doodled planner on warm paper
- [**TWOMUCH.STUDIO**](design-md/twomuch-studio/) - floating museum of curiosities
- [**Uber**](design-md/uber-refero/) - Black-and-white transit kiosk. Picture a monochrome wayfinding panel where the only color comes from editorial illust...
- [**Ui**](design-md/ui/) - clinical blueprint on frosted paper
- [**v0 by Vercel**](design-md/v0-by-vercel/) - A Machinist's Blueprint. Precision and function are paramount, with every element serving a clear purpose on a clean,...
- [**Valo**](design-md/valo/) - noir observatory at midnight — weight-300 typography floats on pure black while a single teal-violet gradient passes...
- [**VEED**](design-md/veed/) - white gallery wall with neon-green ignition buttons
- [**Ventriloc**](design-md/ventriloc/) - Editorial data observatory on warm paper — a single orange ember punctuating monochrome precision.
- [**Vercel**](design-md/vercel-refero/) - Typeset terminal on white paper
- [**Visitors**](design-md/visitors/) - white engineering blueprint
- [**Vivid+Co**](design-md/vivid-co/) - prismatic light through obsidian
- [**Voiceflow**](design-md/voiceflow/) - editorial whiteboard under daylight — serif whispers, pill controls glow blue.
- [**Walden**](design-md/walden/) - A still forest floor — every product is a stone, every pixel is moss and silence.
- [**Warp**](design-md/warp-refero/) - obsidian command center — a developer's IDE cockpit where the only glow is a single violet phosphor on matte black, a...
- [**WHOOP**](design-md/whoop/) - Performance laboratory at midnight — clinical white lab benches beneath a black theatrical void, one violet pulse of...
- [**Wise**](design-md/wise-refero/) - deep moss with lime voltage. Lime sparks on a near-black forest floor, with massive blocky display type announcing ev...
- [**Wise Design**](design-md/wise-design/) - Neon market stall on a global street — electric lime signage that shouts across a crowded marketplace, then polished...
- [**WRITER**](design-md/writer/) - editorial AI atelier — a white marble newsroom where pill-shaped controls and a single violet accent turn enterprise...
- [**xAI**](design-md/xai/) - warm cream laboratory with a black pill
- [**Your workplace has the answer. Just ask Dala for it.**](design-md/your-workplace-has-the-answer-just-ask-dala-for-it/) - constellation floating on black velvet
<!-- refero-styles:end -->

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- **Improve existing files**: Fix wrong colors, missing tokens, weak descriptions
- **Report issues**: Let us know if something looks off

Before opening a PR, please [open an issue](https://github.com/VoltAgent/awesome-design-md/issues) first to discuss your idea and get feedback from maintainers.


## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of design system documents extracted from public websites. All DESIGN.md files are provided "as is" without warranty. The extracted design tokens represent publicly visible CSS values. We do not claim ownership of any site's visual identity. These documents exist to help AI agents generate consistent UI.

// Modern Gaming Marketing Website JavaScript

// ============================================
// i18n Dictionary (EN / KO) — default EN
// Numbers/stats stay as-is; only labels translate.
// ============================================
const i18n = {
    en: {
        'nav.services': 'Services',
        'nav.benefits': 'Benefits',
        'nav.pricing': 'Pricing',
        'nav.cases': 'Case Studies',
        'nav.faq': 'FAQ',
        'nav.bookCall': 'Book a Call',

        'hero.title': 'Save Your 100 Hours of Marketing',
        'hero.subtitle': 'Focus on what you love — game development. We handle the marketing.',
        'hero.tagline': 'Pause or cancel anytime.',
        'hero.seePricing': 'See Pricing',
        'hero.bookCall': 'Book a Call',

        'logos.text': 'Trusted by indie developers worldwide',

        'stats.title': 'Proof in Numbers',
        'stats.subtitle': 'Five years of Steam marketing, measured in results — not promises.',
        'stats.titlesPartnered': 'Titles Partnered',
        'stats.globalMarkets': 'Countries Reached',
        'stats.avgWishlist': 'Avg. Wishlist Growth',
        'stats.yearsValue': '5+',
        'stats.yearsExp': 'Years of Steam Marketing',

        'how.title': 'How it works',
        'how.subtitle': 'Steam marketing, simplified. One flat monthly fee. No surprises.',
        'how.step1Title': 'Subscribe & Share',
        'how.step1Desc': 'Subscribe and get your own Notion page. Share your game details, key milestones, and marketing needs — all in one place.',
        'how.step2Title': 'We Get to Work',
        'how.step2Desc': "We'll build your marketing roadmap: target audience, press, social media management, influencer outreach — you can track every step in real-time.",
        'how.step3Title': 'Grow Your Game',
        'how.step3Desc': "More visibility. More wishlists. More players. You focus on development — we'll handle the buzz.",

        'services.title': 'What We Do',
        'services.subtitle': "Six core services that cover your game's entire marketing journey.",
        'services.s1Title': 'Social Media Management',
        'services.s1Desc': 'Build presence on X, Reddit, TikTok, YouTube, and more — where your audience actually hangs out',
        'services.s2Title': 'Press Release',
        'services.s2Desc': 'Put your game in front of the right audience. We craft and distribute press releases through 60+ gaming and tech media outlets in 11 countries.',
        'services.s3Title': 'Online Event Support',
        'services.s3Desc': 'Get more from every event. From finding the right Steam and third-party opportunities to broadcasting and event amplification, we help maximize your reach and results.',
        'services.s4Title': 'Paid Social Ads',
        'services.s4Desc': 'Reddit, TikTok, and YouTube campaigns, optimized with Steam Analytics for real, measurable wishlist conversion.',
        'services.s5Title': 'Steam Page Optimization',
        'services.s5Desc': 'Better descriptions, smarter tags, and higher Steam discoverability — plus hands-on feedback on your capsule image and trailer.',
        'services.s6Title': 'Content Creator Outreach',
        'services.s6Desc': 'We introduce your game to YouTubers and streamers whose audiences already enjoy games like yours, creating opportunities for organic coverage.',
        'services.cta': 'Book a Call',

        'results.title': 'Case Studies',
        'results.subtitle': 'See how our marketing strategies helped indie games grow.',
        'results.before': 'Before',
        'results.strategy': 'What We Changed',
        'results.results': 'Results',
        'results.case1Badge': 'Case 1 · Community Strategy',
        'results.case1Title': 'From Costly Ads to a Growing Community',
        'results.case1Before1': 'Paid advertising campaigns with low engagement',
        'results.case1Before2': 'Broad Steam tags limiting visibility among target players',
        'results.case1Before3': 'Limited participation in online events',
        'results.case1Strategy1': 'Optimized targeting through competitor and genre analysis',
        'results.case1Strategy2': 'Community-driven social marketing across platforms such as Reddit',
        'results.case1Strategy3': 'Active participation in online showcases',
        'results.case1M1': 'Steam Impressions',
        'results.case1M2': 'Page Visits',
        'results.case1M3': 'Wishlists',
        'results.case2Badge': 'Case 2 · Ad Channel Optimization',
        'results.case2Title': 'Smarter Ad Spend, Better Results',
        'results.case2Before1': 'Advertising budget spread across multiple platforms',
        'results.case2Before2': 'Limited optimization based on platform performance',
        'results.case2Before3': 'No focused strategy for reaching high-intent players',
        'results.case2Strategy1': 'Reallocated budget based on channel performance analysis',
        'results.case2Strategy2': 'Focused on highly targeted Reddit campaigns',
        'results.case2Strategy3': 'Used TikTok to expand reach and drive additional traffic',
        'results.case2Strategy4': 'Concentrated Google Ads on top-performing regions',
        'results.case2M1': 'TikTok CPC',
        'results.case2M2': 'Reddit CPC',
        'results.case2M3': 'Google CPV',

        'why.title': 'Why Choose Us',
        'why.subtitle': "Focus on building your game. We'll help it get discovered.",
        'why.f1Title': 'Gamer & Developer Marketers',
        'why.f1Desc': "Built by people who've shipped games themselves. We understand the challenges, priorities, and realities of indie development.",
        'why.f2Title': 'Global Reach',
        'why.f2Desc': 'Reach players worldwide through our network of media, creators, and gaming communities across 15+ countries.',
        'why.f3Title': 'Data-Driven Strategy',
        'why.f3Desc': 'Every decision is guided by Steam Analytics, campaign performance, and player behavior — not assumptions.',
        'why.f4Title': 'Fast Execution',
        'why.f4Desc': 'Launch windows don\'t wait. We onboard quickly and execute when timing matters most.',
        'why.f5Title': 'Transparent Partnership',
        'why.f5Desc': "No black box marketing. Follow every task, update, and result through a shared workspace.",
        'why.f6Title': 'Indie-Focused Experience',
        'why.f6Desc': "Five years in indie games. We know what works — and what doesn't.",

        'pricing.title': 'Plans',
        'pricing.popular': 'Most Popular',
        'pricing.plan1Name': 'Starter',
        'pricing.plan1Price': '$1,800/mo',
        'pricing.plan1Desc': 'Build your foundation and start reaching the right players.',
        'pricing.plan1F1': '✔️ Audience & Competitor Research',
        'pricing.plan1F2': '✔️ X & Reddit Management',
        'pricing.plan1F3': '✔️ Influencer Discovery & Outreach on X',
        'pricing.plan1F4': '✔️ Steam & 3rd Party Online Event Support',
        'pricing.plan1F5': '✔️ Event Amplification & Broadcasting',
        'pricing.plan1F6': '✔️ Monthly Performance Report',
        'pricing.plan2Name': 'Momentum',
        'pricing.plan2Price': '$3,500/mo',
        'pricing.plan2Desc': 'Expand your reach across multiple channels and build launch momentum.',
        'pricing.plan2F1': 'Everything in Starter, plus:',
        'pricing.plan2F2': '✔️ Launch Marketing Roadmap',
        'pricing.plan2F3': '✔️ Steam Store Page Review',
        'pricing.plan2F4': '✔️ Milestone-Based Media Outreach',
        'pricing.plan2F5': '✔️ TikTok Management',
        'pricing.plan2F6': '✔️ YouTube Shorts Management',
        'pricing.plan2F7': '✔️ Weekly Performance Report',
        'pricing.plan3Name': 'Scale',
        'pricing.plan3Price': '$5,500/mo',
        'pricing.plan3Desc': 'A fully managed growth plan for teams that want to maximize visibility, wishlists, and launch performance.',
        'pricing.plan3F1': 'Everything in Momentum, plus:',
        'pricing.plan3F2': '✔️ Steam Marketing Strategy',
        'pricing.plan3F3': '✔️ Steam Page Optimization',
        'pricing.plan3F4': '✔️ Wishlist Conversion Optimization',
        'pricing.plan3F5': '✔️ Capsule & Trailer Feedback',
        'pricing.plan3F6': '✔️ Creator Outreach',
        'pricing.plan3F7': '✔️ Paid Ad Campaign Management',
        'pricing.plan3F8': '✔️ Dedicated Strategy Sessions',
        'pricing.plan3F9': '✔️ Priority Support',
        'pricing.note': 'Ad spend for paid press and paid ads is billed separately. Prices exclude VAT.',

        'process.title': 'Our Process',
        'process.subtitle': 'From understanding your game to reaching more players, our process keeps every step clear and focused on results.',
        'process.p1Title': 'Discovery',
        'process.p1Desc': 'We learn about your game, goals, audience, and competitive landscape.',
        'process.p2Title': 'Strategy',
        'process.p2Desc': 'We build a tailored marketing roadmap based on your genre, audience, and launch plans.',
        'process.p3Title': 'Content Creation',
        'process.p3Desc': 'We create content and messaging designed to attract players and drive engagement.',
        'process.p4Title': 'Launch & Promotion',
        'process.p4Desc': 'We launch campaigns across social media, press, creators, and events.',
        'process.p5Title': 'Optimization',
        'process.p5Desc': 'We monitor performance and continuously refine campaigns based on real data.',
        'process.p6Title': 'Reporting & Insights',
        'process.p6Desc': 'Regular reports and recommendations keep you informed and moving forward.',
        'faq.title': 'FAQ',
        'faq.q1': 'Do I need to have a Steam page already?',
        'faq.a1': 'Yes, or at least be ready to launch one with us during the first month.',
        'faq.q2': 'Do I need to share a demo of my game?',
        'faq.a2': 'Yes — to understand your game and create content effectively, we need access to a playable build.',
        'faq.q3': 'Do you manage paid ads?',
        'faq.a3': 'Yes. Once we align on campaign goals and budget, we handle setup, optimization, and management.',
        'faq.q4': 'Do you create trailers?',
        'faq.a4': "We don't produce trailers ourselves, but we're happy to give you feedback on yours. For cinematic trailers, we recommend working with a specialized studio.",
        'faq.q5': 'Do you only work with Steam games? What about mobile?',
        'faq.a5': 'We specialize in PC/Steam games. At this time, we do not support mobile game marketing.',
        'faq.q6': 'How do I communicate and track progress?',
        'faq.a6': "Once you sign up, you'll get access to a dedicated Notion page. There, you can share info, track tasks, view updates, and communicate directly with us — all in one place.",
        'faq.q7': "Who's behind this service?",
        'faq.a7': "We're a four-person team of English-speaking Korean and Russian professionals. We've built and launched our own turn-based strategy and action games, handling everything from development to marketing and publishing. With over 10 years in the game industry, we now help other indie devs do the same.",

        'footer.tagline': 'Focus on development. We handle the marketing.',
        'footer.ready': 'Ready to grow your game?',
        'footer.getStarted': 'Book a Free Consultation'
    },
    ko: {
        'nav.services': '서비스',
        'nav.benefits': '강점',
        'nav.pricing': '가격',
        'nav.cases': '사례',
        'nav.faq': 'FAQ',
        'nav.bookCall': '상담 예약',

        'hero.title': '마케팅에 쓸 100시간을 돌려드립니다',
        'hero.subtitle': '게임 개발에만 집중하세요. 마케팅은 저희가 맡습니다.',
        'hero.tagline': '구독형 서비스, 언제든 일시정지·해지 가능합니다.',
        'hero.seePricing': '가격 보기',
        'hero.bookCall': '상담 예약',

        'logos.text': '전 세계 인디 개발자들이 함께합니다',

        'stats.title': '숫자로 증명합니다',
        'stats.subtitle': '5년간의 Steam 마케팅, 약속이 아닌 결과로 말합니다.',
        'stats.titlesPartnered': '파트너 타이틀',
        'stats.globalMarkets': '진출 국가',
        'stats.avgWishlist': '평균 위시리스트 증가',
        'stats.yearsValue': '5년+',
        'stats.yearsExp': 'Steam 마케팅 경력',

        'how.title': 'How it works',
        'how.subtitle': 'Steam 마케팅이 이렇게 단순해집니다. 월 정액 하나로, 숨은 비용 없이.',
        'how.step1Title': '구독 & 게임 정보 공유',
        'how.step1Desc': '서비스를 구독하면 전용 Notion 페이지가 제공됩니다. 게임 정보, 주요 개발 일정, 마케팅 요청 사항을 한곳에서 손쉽게 공유하세요.',
        'how.step2Title': '마케팅 시작',
        'how.step2Desc': '타겟 유저 분석부터 언론 홍보, 소셜미디어 운영, 인플루언서 협업까지. 게임에 맞는 마케팅 전략을 수립하고, 모든 진행 상황을 실시간으로 확인할 수 있습니다.',
        'how.step3Title': '게임 성장',
        'how.step3Desc': '더 많은 노출, 더 많은 위시리스트, 더 많은 플레이어. 개발에만 집중하세요. 게임을 알리는 일은 저희가 맡겠습니다.',

        'services.title': 'What We Do',
        'services.subtitle': '게임 마케팅의 처음부터 끝까지, 6가지 핵심 서비스로 커버합니다.',
        'services.s1Title': '소셜 미디어 운영',
        'services.s1Desc': 'X, Reddit, TikTok, YouTube 등 게임에 관심을 가질 플레이어들이 활동하는 채널에서 인지도를 높이고 커뮤니티를 성장시킵니다.',
        'services.s2Title': '보도자료',
        'services.s2Desc': '게임을 소개해야 할 곳에 정확히 알립니다. 11개국 60개 이상의 게임 전문 매체를 통해 게임 소식을 전 세계 플레이어에게 전달합니다.',
        'services.s3Title': '온라인 이벤트 지원',
        'services.s3Desc': '게임에 맞는 Steam 및 외부 이벤트를 발굴하고, Broadcasting과 소셜 미디어 홍보를 통해 더 많은 관심과 참여를 이끌어냅니다.',
        'services.s4Title': '유료 소셜미디어 광고',
        'services.s4Desc': 'Reddit, TikTok, YouTube 광고 캠페인을 Steam Analytics 데이터와 연동해 실질적인 위시리스트 전환으로 최적화합니다.',
        'services.s5Title': 'Steam 페이지 최적화',
        'services.s5Desc': '설명 문구와 태그를 다듬어 Steam 내 검색 노출을 높입니다. 캡슐 이미지·트레일러 개선 컨설팅도 함께 진행합니다.',
        'services.s6Title': '크리에이터 발굴 및 홍보',
        'services.s6Desc': '내 게임을 좋아할 가능성이 높은 크리에이터를 발굴하고, 게임을 소개해 플레이와 콘텐츠 제작을 유도합니다.',
        'services.cta': '상담 예약',

        'results.title': 'Case Studies',
        'results.subtitle': '인디게임의 성장을 만들어낸 실제 사례를 살펴보세요.',
        'results.before': 'Before',
        'results.strategy': 'What We Changed',
        'results.results': 'Results',
        'results.case1Badge': '사례 1 · 커뮤니티 전략',
        'results.case1Title': '광고비 낭비를 줄이고 커뮤니티를 키웠습니다',
        'results.case1Before1': '낮은 참여율의 유료 광고 캠페인 운영',
        'results.case1Before2': '범용 태그 중심의 스팀 페이지 구성으로 타겟 유저 도달 한계',
        'results.case1Before3': '온라인 이벤트 참석 및 게임 커뮤니티 활동 부족',
        'results.case1Strategy1': '유사 게임 분석 기반의 타겟 유저 및 태그 최적화',
        'results.case1Strategy2': 'Reddit 중심의 커뮤니티 기반 소셜 마케팅',
        'results.case1Strategy3': 'Steam 행사 및 온라인 이벤트 적극 활용',
        'results.case1M1': 'Steam 노출',
        'results.case1M2': '페이지 방문',
        'results.case1M3': '위시리스트',
        'results.case2Badge': '사례 2 · 광고 채널 최적화',
        'results.case2Title': '광고비는 그대로, 성과는 더 크게 만들었습니다',
        'results.case2Before1': '광고 예산이 여러 플랫폼에 분산되어 운영됨',
        'results.case2Before2': '플랫폼별 성과 차이에 따른 최적화 부족',
        'results.case2Before3': '타겟 플레이어에게 집중된 유입 전략 부재',
        'results.case2Strategy1': '플랫폼별 성과 분석을 기반으로 광고 예산 재배분',
        'results.case2Strategy2': 'Reddit 중심의 정밀 타겟팅 캠페인 운영',
        'results.case2Strategy3': 'TikTok을 활용한 추가 트래픽 확보 및 인지도 확산',
        'results.case2Strategy4': 'Google 광고는 성과가 높은 국가 및 지역 중심으로 집중 운영',
        'results.case2M1': 'TikTok CPC',
        'results.case2M2': 'Reddit CPC',
        'results.case2M3': 'Google CPV',

        'why.title': '왜 HypePotions인가',
        'why.subtitle': '게임 개발에 집중하세요. 마케팅은 HypePotions가 함께합니다.',
        'why.f1Title': '게이머이자 개발자인 마케터',
        'why.f1Desc': '저희는 마케터이기 전에 게임 개발자입니다. 그래서 인디 개발자가 무엇을 고민하는지, 무엇이 필요한지 잘 알고 있습니다.',
        'why.f2Title': '글로벌 네트워크',
        'why.f2Desc': '15개국 이상의 매체, 크리에이터, 게임 커뮤니티 네트워크를 통해 전 세계 플레이어에게 게임을 알립니다.',
        'why.f3Title': '데이터 기반 전략',
        'why.f3Desc': 'Steam Analytics, 캠페인 성과, 플레이어 데이터를 바탕으로 전략을 수립합니다. 감이 아닌 데이터로 판단합니다.',
        'why.f4Title': '빠른 실행',
        'why.f4Desc': '출시 기회는 기다려주지 않습니다. 중요한 순간을 놓치지 않도록 빠르게 시작하고 실행합니다.',
        'why.f5Title': '투명한 파트너십',
        'why.f5Desc': '무엇을 하고 있는지 알 수 없는 마케팅은 없습니다. 모든 진행 상황과 결과를 실시간으로 공유합니다.',
        'why.f6Title': '인디 게임 전문',
        'why.f6Desc': '인디게임 마케팅만 5년. 무엇이 통하고 무엇이 통하지 않는지 알고 있습니다.',

        'pricing.title': '요금제',
        'pricing.popular': '가장 인기',
        'pricing.plan1Name': 'Starter',
        'pricing.plan1Price': '월 250만원',
        'pricing.plan1Desc': '게임에 관심을 가질 플레이어를 찾고, 꾸준한 노출을 시작하는 플랜입니다.',
        'pricing.plan1F1': '✔️ 타겟 플레이어 및 경쟁작 분석',
        'pricing.plan1F2': '✔️ X 및 Reddit 콘텐츠 운영',
        'pricing.plan1F3': '✔️ X 내 인플루언서 발굴 및 게임 소개',
        'pricing.plan1F4': '✔️ Steam 및 3rd Party 온라인 이벤트 참가 지원',
        'pricing.plan1F5': '✔️ 이벤트 참가 홍보 및 방송 지원',
        'pricing.plan1F6': '✔️ 월간 성과 리포트',
        'pricing.plan2Name': 'Momentum',
        'pricing.plan2Price': '월 500만원',
        'pricing.plan2Desc': '출시를 앞두고 더 많은 플레이어에게 게임을 알리는 플랜입니다.',
        'pricing.plan2F1': 'Everything in Starter, plus:',
        'pricing.plan2F2': '✔️ 출시 마케팅 로드맵 수립',
        'pricing.plan2F3': '✔️ Steam 페이지 진단 및 개선 제안',
        'pricing.plan2F4': '✔️ 마일스톤 기반 보도자료 배포 및 매체 홍보',
        'pricing.plan2F5': '✔️ TikTok 콘텐츠 운영',
        'pricing.plan2F6': '✔️ YouTube Shorts 제작 및 운영',
        'pricing.plan2F7': '✔️ 주간 성과 리포트',
        'pricing.plan3Name': 'Scale',
        'pricing.plan3Price': '월 800만원',
        'pricing.plan3Desc': '마케팅 전반을 맡기고 개발에 집중하고 싶은 팀을 위한 플랜입니다.',
        'pricing.plan3F1': 'Everything in Momentum, plus:',
        'pricing.plan3F2': '✔️ 스팀 마케팅 전략 수립',
        'pricing.plan3F3': '✔️ Steam 페이지 최적화',
        'pricing.plan3F4': '✔️ 위시리스트 전환율 최적화',
        'pricing.plan3F5': '✔️ 캡슐 이미지 및 트레일러 피드백',
        'pricing.plan3F6': '✔️ 크리에이터 발굴 및 홍보',
        'pricing.plan3F7': '✔️ 유료 광고 캠페인 운영 및 최적화',
        'pricing.plan3F8': '✔️ 전담 전략 미팅',
        'pricing.plan3F9': '✔️ 우선 응대 및 전담 상담',
        'pricing.note': '유료 보도자료 및 유료 광고의 실제 광고비는 별도 청구됩니다. 부가세 별도.',

        'process.title': '진행 프로세스',
        'process.subtitle': '게임을 이해하는 것부터 플레이어에게 알리는 것까지. 검증된 프로세스로 마케팅을 체계적으로 진행합니다.',
        'process.p1Title': '게임 분석',
        'process.p1Desc': '게임의 강점과 목표, 타겟 플레이어, 경쟁작을 분석합니다.',
        'process.p2Title': '전략 수립',
        'process.p2Desc': '장르와 타겟 플레이어, 출시 계획에 맞는 마케팅 전략을 수립합니다.',
        'process.p3Title': '콘텐츠 제작',
        'process.p3Desc': '플레이어의 관심을 끌고 참여를 유도할 콘텐츠를 제작합니다.',
        'process.p4Title': '캠페인 실행',
        'process.p4Desc': '소셜 미디어, 게임 매체, 크리에이터, 이벤트를 통해 게임을 알립니다.',
        'process.p5Title': '성과 최적화',
        'process.p5Desc': '실제 데이터를 바탕으로 성과를 분석하고 지속적으로 개선합니다.',
        'process.p6Title': '성과 리포트',
        'process.p6Desc': '성과 리포트와 개선 제안을 통해 다음 단계를 함께 준비합니다.',
        'faq.title': '자주 묻는 질문',
        'faq.q1': '이미 Steam 페이지가 있어야 하나요?',
        'faq.a1': '네. 또는 첫 달 안에 저희와 함께 페이지를 개설할 준비가 되어 있으면 됩니다.',
        'faq.q2': '게임 데모를 공유해야 하나요?',
        'faq.a2': '네 — 게임을 제대로 이해하고 효과적인 콘텐츠를 만들려면 플레이 가능한 빌드가 필요합니다.',
        'faq.q3': '유료 광고 운영도 하나요?',
        'faq.a3': '네. 캠페인 목표와 예산을 함께 정한 뒤, 셋업·최적화·운영까지 전부 진행합니다.',
        'faq.q4': '트레일러도 제작하나요?',
        'faq.a4': '트레일러를 직접 제작하지는 않지만, 보유하신 트레일러에 대한 피드백은 기꺼이 드립니다. 시네마틱 트레일러는 전문 스튜디오와 협업하시길 권합니다.',
        'faq.q5': 'Steam 게임만 하나요? 모바일은요?',
        'faq.a5': '저희는 PC/Steam 게임 전문입니다. 현재 모바일 게임 마케팅은 지원하지 않습니다.',
        'faq.q6': '진행 상황은 어떻게 확인하나요?',
        'faq.a6': '가입 후 전용 Notion 페이지가 제공됩니다. 정보 공유, 작업 현황, 업데이트 확인, 직접 소통까지 한곳에서 가능합니다.',
        'faq.q7': '운영 팀이 어떻게 구성되어 있나요?',
        'faq.a7': '영어가 가능한 한국인과 러시아인으로 구성된 4인 팀입니다. 자체 턴제 전략·액션 게임을 개발·출시하며 개발부터 마케팅, 퍼블리싱까지 모두 다뤘습니다. 게임 업계 10년 이상의 경험을 바탕으로 이제 다른 인디 개발자들을 돕고 있습니다.',

        'footer.tagline': '개발에만 집중하세요. 마케팅은 저희가 맡습니다.',
        'footer.ready': '게임을 성장시킬 준비가 되셨나요?',
        'footer.getStarted': '무료 상담 예약하기'
    }
};

// Apply a language to all [data-i18n] elements
function applyLanguage(lang) {
    const dict = i18n[lang] || i18n.en;
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key] !== undefined) {
            el.textContent = dict[key];
        }
    });
    document.documentElement.lang = lang;
    // Button shows the language you can switch TO
    const toggle = document.getElementById('langToggle');
    if (toggle) {
        toggle.textContent = lang === 'en' ? 'KO' : 'EN';
    }
    localStorage.setItem('lang', lang);
}

function initLanguage() {
    const saved = localStorage.getItem('lang') || 'en';
    applyLanguage(saved);

    const toggle = document.getElementById('langToggle');
    if (toggle) {
        toggle.addEventListener('click', () => {
            const current = localStorage.getItem('lang') || 'en';
            applyLanguage(current === 'en' ? 'ko' : 'en');
        });
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Language toggle (KO/EN)
    initLanguage();

    // Navigation functionality
    initNavigation();

    // FAQ Accordion functionality
    initFAQ();

    // Smooth scrolling for CTA buttons
    initSmoothScrolling();

    // Scroll animations
    initScrollAnimations();

    // Interactive effects
    initInteractiveEffects();

    // Pricing card animations
    initPricingAnimations();

    // Active section highlighting
    initActiveSection();
});

// Navigation functionality - Fixed
function initNavigation() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Mobile menu toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }
    
    // Handle nav link clicks with proper scrolling
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Close mobile menu
            if (navToggle && navMenu) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            }
            
            // Get target section and scroll to it
            const targetHref = link.getAttribute('href');
            const targetElement = document.querySelector(targetHref);
            
            if (targetElement) {
                const headerOffset = 100; // Account for fixed navbar
                const elementPosition = targetElement.offsetTop;
                const offsetPosition = elementPosition - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
        if (navToggle && navMenu && !navToggle.contains(e.target) && !navMenu.contains(e.target)) {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        }
    });
}

// FAQ Accordion
function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Close all FAQ items
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('active');
                const otherAnswer = otherItem.querySelector('.faq-answer');
                otherAnswer.style.maxHeight = '0px';
            });
            
            // Toggle current item
            if (!isActive) {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });
}

// Smooth scrolling for CTA buttons
function initSmoothScrolling() {
    const ctaButtons = document.querySelectorAll('.cta-btn[data-target]');
    
    ctaButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = button.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerOffset = 100; // Account for any fixed header
                const elementPosition = targetElement.offsetTop;
                const offsetPosition = elementPosition - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Scroll animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.step-card, .feature-card, .service-card, .pricing-card, .stat-card, .result-card, .process-step');
    animateElements.forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });
}

// Interactive effects
function initInteractiveEffects() {
    // Add hover effects to cards
    const cards = document.querySelectorAll('.step-card, .feature-card, .service-card, .pricing-card, .stat-card, .result-card, .process-step');
    
    cards.forEach(card => {
        let originalTransform = '';
        
        card.addEventListener('mouseenter', () => {
            originalTransform = card.style.transform || '';
            if (card.classList.contains('pricing-card--featured')) {
                card.style.transform = 'scale(1.05) translateY(-5px)';
            } else {
                card.style.transform = 'translateY(-5px)';
            }
        });
        
        card.addEventListener('mouseleave', () => {
            if (card.classList.contains('pricing-card--featured')) {
                card.style.transform = 'scale(1.05)';
            } else {
                card.style.transform = '';
            }
        });
    });
    
    // Button hover effects
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', () => {
            button.style.transform = '';
        });
    });
}

// Pricing card animations
function initPricingAnimations() {
    const pricingCards = document.querySelectorAll('.pricing-card');
    
    pricingCards.forEach((card, index) => {
        // Stagger animation
        card.style.animationDelay = `${index * 0.1}s`;
        
        // Add click effect
        card.addEventListener('click', () => {
            const currentTransform = card.style.transform;
            card.style.transform = currentTransform + ' scale(0.98)';
            setTimeout(() => {
                card.style.transform = currentTransform;
            }, 150);
        });
    });
}

// Active section highlighting
function initActiveSection() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '-100px 0px -50% 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.getAttribute('id');
                
                // Remove active class from all nav links
                navLinks.forEach(link => link.classList.remove('active'));
                
                // Add active class to current section's nav link
                const activeLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        observer.observe(section);
    });
}

// Additional utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Navbar scroll effect
window.addEventListener('scroll', debounce(() => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 4px 12px rgba(26, 26, 26, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 1px 3px rgba(26, 26, 26, 0.1)';
    }
}, 10));

// Loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
    
    // Animate hero content
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        heroContent.style.opacity = '0';
        heroContent.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            heroContent.style.transition = 'all 0.8s ease-out';
            heroContent.style.opacity = '1';
            heroContent.style.transform = 'translateY(0)';
        }, 300);
    }
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');
        if (navToggle && navMenu) {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        }
        
        // Close all FAQ items
        const faqItems = document.querySelectorAll('.faq-item');
        faqItems.forEach(item => {
            item.classList.remove('active');
            const answer = item.querySelector('.faq-answer');
            if (answer) {
                answer.style.maxHeight = '0px';
            }
        });
    }
});

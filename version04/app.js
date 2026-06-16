// Modern Gaming Marketing Website JavaScript

// ============================================
// i18n Dictionary (EN / KO) — default EN
// Numbers/stats stay as-is; only labels translate.
// ============================================
const i18n = {
    en: {
        'nav.proof': 'Proof',
        'nav.services': 'Services',
        'nav.benefits': 'Benefits',
        'nav.pricing': 'Pricing',
        'nav.bookCall': 'Book a Call',

        'hero.title': 'Save Your 100 Hours of Marketing',
        'hero.subtitle': 'Focus on what you love — game development. We handle the marketing.',
        'hero.tagline': 'Fixed-term contracts — you know the scope, the timeline, and exactly what you get.',
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
        'how.step2Desc': "We'll build your marketing roadmap: target audience, press, influencer outreach — you can track every step in real-time.",
        'how.step3Title': 'Grow Your Game',
        'how.step3Desc': "More visibility. More wishlists. More players. You focus on development — we'll handle the buzz.",

        'services.title': 'What We Do',
        'services.subtitle': "Six core services that cover your game's entire marketing journey.",
        'services.s1Title': 'Social Media Management',
        'services.s1Desc': 'X, Reddit, TikTok, and YouTube — we build and run your channels and community, driving an average +536% follower growth.',
        'services.s2Title': 'Press Release & PR',
        'services.s2Desc': 'We distribute to 60+ outlets across 11 countries and 7 languages — including Rock Paper Shotgun, Famitsu, 4Gamer, and Gematsu. Averaging 20+ pickups per title.',
        'services.s3Title': 'Online Event Support',
        'services.s3Desc': 'Steam Next Fest, Steam Sales, and third-party events — we apply, prepare, and maximize every opportunity.',
        'services.s4Title': 'Paid Social Ads',
        'services.s4Desc': 'Reddit, TikTok, and YouTube campaigns, optimized with Steam Analytics for real, measurable wishlist conversion.',
        'services.s5Title': 'Steam Page Optimization',
        'services.s5Desc': 'Better descriptions, smarter tags, and higher Steam discoverability — plus hands-on feedback on your capsule image and trailer.',
        'services.s6Title': 'Content Creator Outreach',
        'services.s6Desc': 'We pitch your game to YouTubers and streamers who already love your genre — real fans, real coverage.',
        'services.cta': 'Book a Call',

        'results.title': 'Real Results',
        'results.subtitle': 'How our strategies turned into measurable growth for indie titles.',
        'results.before': 'Before',
        'results.strategy': 'Strategy',
        'results.after': 'After',
        'results.results': 'Results',
        'results.case1Badge': 'Case 1 · Community Strategy',
        'results.case1Title': 'From Wasted Ads to a Thriving Community',
        'results.case1Before': 'Budget going to ads that built no community. Tags were too generic to reach the right players.',
        'results.case1Strategy': 'Precision targeting, a Reddit-centered community, and Japanese influencer outreach.',
        'results.case1M1': 'Steam Impressions',
        'results.case1M2': 'Page Visits',
        'results.case1M3': 'Wishlists',
        'results.case2Badge': 'Case 2 · Ad Channel Optimization',
        'results.case2Title': 'Squeezing Maximum Reach From Every Dollar',
        'results.case2Before': 'Google burned budget with the weakest traffic efficiency. TikTok was cheap but barely converted. Reddit delivered the best targeting at a reasonable cost.',
        'results.case2Strategy': 'Reallocated budget to the highest-performing channels — 75% Reddit, 25% TikTok — based on live cost data.',
        'results.case2M1': 'TikTok CPC',
        'results.case2M2': 'Reddit CPC',
        'results.case2M3': 'Google CPV',

        'why.title': 'Why Choose Us',
        'why.subtitle': "Smart, flexible marketing for indie devs who'd rather build than hustle.",
        'why.f1Title': 'Gamer & Developer Marketers',
        'why.f1Desc': "We're not just marketers — we're gamers and devs who've shipped our own titles. We speak your language.",
        'why.f2Title': 'Global Network',
        'why.f2Desc': '15+ countries of media, influencer, and community reach — your game goes worldwide from day one.',
        'why.f3Title': 'Data-Driven Strategy',
        'why.f3Desc': 'Every decision is backed by Steam Analytics and live campaign data — no guesswork, just results.',
        'why.f4Title': 'Fast Execution',
        'why.f4Desc': 'Onboarding in 3–5 business days. We move at the speed your launch window demands.',
        'why.f5Title': 'Transparent Partnership',
        'why.f5Desc': "One flat fee, a shared Notion HQ, and weekly updates. You always know exactly what we're doing.",
        'why.f6Title': 'Indie-Specialized Experience',
        'why.f6Desc': "Five years and 20+ titles focused entirely on indie Steam games — we know what works and what doesn't.",

        'pricing.title': 'Plans',
        'pricing.popular': 'Most Popular',
        'pricing.plan1Name': 'Starter',
        'pricing.plan1Price': '$1,800/mo',
        'pricing.plan1Desc': 'Core visibility — without the agency overhead.',
        'pricing.plan1F1': '✔️ Online festival applications & participation',
        'pricing.plan1F2': '✔️ Press release (1x per month)',
        'pricing.plan1F3': '✔️ Twitter & Reddit post management',
        'pricing.plan1F4': '✔️ Audience & competitor research',
        'pricing.plan1F5': '✔️ Dedicated Notion workspace',
        'pricing.plan1F6': '✔️ Monthly performance report',
        'pricing.plan2Name': 'Momentum',
        'pricing.plan2Price': '$3,500/mo',
        'pricing.plan2Desc': 'Full-channel reach — built for your launch push.',
        'pricing.plan2F1': '✔️ Everything in Starter, plus:',
        'pricing.plan2F2': '✔️ TikTok content strategy & posting',
        'pricing.plan2F3': '✔️ YouTube shorts & clips',
        'pricing.plan2F4': '✔️ Content creator outreach',
        'pricing.plan2F5': '✔️ Discord server setup & community management',
        'pricing.plan2F6': '✔️ Online event support (Next Fest, sales, etc.)',
        'pricing.plan3Name': 'Scale',
        'pricing.plan3Price': '$5,500/mo',
        'pricing.plan3Desc': 'Paid ads, page optimization, and priority access — fully managed.',
        'pricing.plan3F1': '✔️ Everything in Momentum, plus:',
        'pricing.plan3F2': '✔️ Paid ad campaign setup & optimization',
        'pricing.plan3F3': '✔️ Steam page optimization',
        'pricing.plan3F4': '✔️ Capsule image & trailer feedback',
        'pricing.plan3F5': '✔️ Priority response & consultation',
        'pricing.plan3F6': '✔️ Dedicated manager & direct line',
        'pricing.note': 'Ad spend for paid press and paid ads is billed separately. Prices exclude VAT.',

        'process.title': 'Our Process',
        'process.subtitle': 'A clear, repeatable path from kickoff to results.',
        'process.p1Title': 'Initial Consultation',
        'process.p1Desc': 'We learn your game, goals, and audience.',
        'process.p2Title': 'Strategy Design',
        'process.p2Desc': 'A tailored roadmap across channels and markets.',
        'process.p3Title': 'Asset Production',
        'process.p3Desc': 'Content, copy, and creatives built to convert.',
        'process.p4Title': 'Campaign Launch',
        'process.p4Desc': 'We go live across press, social, and ads.',
        'process.p5Title': 'Monitoring',
        'process.p5Desc': 'Live optimization based on real performance data.',
        'process.p6Title': 'Reporting',
        'process.p6Desc': 'Monthly reports plus weekly updates, always transparent.',
        'process.note': 'Average onboarding: 3–5 business days · Monthly reports + weekly updates · A dedicated 1:1 manager',

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
        'faq.a7': "We're an English-speaking Korean and Russian two-person team. As part of a 5-person dev team, we've built and launched our own turn-based strategy and action games, handling everything from development to marketing and publishing. With over 10 years in the game industry, we now help other indie devs do the same.",

        'footer.tagline': 'Focus on development. We handle the marketing.',
        'footer.ready': 'Ready to grow your game?',
        'footer.getStarted': 'Schedule Your Free Strategy Session'
    },
    ko: {
        'nav.proof': '실적',
        'nav.services': '서비스',
        'nav.benefits': '강점',
        'nav.pricing': '가격',
        'nav.bookCall': '상담 예약',

        'hero.title': '마케팅에 쓸 100시간을 돌려드립니다',
        'hero.subtitle': '게임 개발에만 집중하세요. 마케팅은 저희가 맡습니다.',
        'hero.tagline': '기간제 계약 방식 — 범위, 일정, 결과물 모두 계약으로 명확히 합니다.',
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

        'how.title': '진행 방식',
        'how.subtitle': 'Steam 마케팅이 이렇게 단순해집니다. 월 정액 하나로, 숨은 비용 없이.',
        'how.step1Title': '계약 후 정보 공유',
        'how.step1Desc': '계약하면 전용 Notion 페이지가 제공됩니다. 게임 정보, 주요 마일스톤, 마케팅 요청 사항을 한곳에 정리해 공유하세요.',
        'how.step2Title': '저희가 바로 시작합니다',
        'how.step2Desc': '타겟 오디언스 분석, 언론 배포, 인플루언서 아웃리치까지 — 마케팅 로드맵을 설계하고, 모든 진행 상황을 실시간으로 확인하실 수 있습니다.',
        'how.step3Title': '게임이 성장합니다',
        'how.step3Desc': '더 많은 노출, 더 많은 위시리스트, 더 많은 플레이어. 개발에만 집중하세요 — 화제 만들기는 저희가 합니다.',

        'services.title': '제공 서비스',
        'services.subtitle': '게임 마케팅의 처음부터 끝까지, 6가지 핵심 서비스로 커버합니다.',
        'services.s1Title': '소셜 미디어 운영',
        'services.s1Desc': 'X, Reddit, TikTok, YouTube 채널과 커뮤니티를 직접 구축·운영합니다. 평균 팔로워 성장률 +536%.',
        'services.s2Title': '보도자료 & PR',
        'services.s2Desc': '11개국·7개 언어·60개 이상 매체 네트워크에 직접 배포합니다. Rock Paper Shotgun, Famitsu, 4Gamer, Gematsu 등 포함. 타이틀당 평균 20건 이상 게재됩니다.',
        'services.s3Title': '온라인 이벤트 지원',
        'services.s3Desc': 'Steam Next Fest, Steam 세일, 서드파티 이벤트 — 신청부터 준비, 결과 극대화까지 모두 맡아 진행합니다.',
        'services.s4Title': '유료 소셜 광고',
        'services.s4Desc': 'Reddit, TikTok, YouTube 광고 캠페인을 Steam Analytics 데이터와 연동해 실질적인 위시리스트 전환으로 최적화합니다.',
        'services.s5Title': 'Steam 페이지 최적화',
        'services.s5Desc': '설명 문구와 태그를 다듬어 Steam 내 검색 노출을 높입니다. 캡슐 이미지·트레일러 개선 컨설팅도 함께 진행합니다.',
        'services.s6Title': '크리에이터 아웃리치',
        'services.s6Desc': '게임 장르를 진심으로 좋아하는 유튜버·스트리머에게 직접 게임을 소개합니다. 진짜 팬, 진짜 커버리지입니다.',
        'services.cta': '상담 예약',

        'results.title': '실제 성과',
        'results.subtitle': '저희 전략이 인디 타이틀의 측정 가능한 성장으로 이어진 실사례입니다.',
        'results.before': 'Before',
        'results.strategy': '전략',
        'results.after': 'After',
        'results.results': '결과',
        'results.case1Badge': '사례 1 · 커뮤니티 전략',
        'results.case1Title': '낭비되던 광고비에서 살아있는 커뮤니티로',
        'results.case1Before': '광고비는 쓰이고 있었지만 커뮤니티로 이어지지 않았습니다. 태그가 너무 범용적이라 핵심 유저에게 닿지 못하고 있었습니다.',
        'results.case1Strategy': '정밀 타겟팅, Reddit 중심 커뮤니티 구축, 일본 인플루언서 아웃리치를 병행했습니다.',
        'results.case1M1': 'Steam 노출',
        'results.case1M2': '페이지 방문',
        'results.case1M3': '위시리스트',
        'results.case2Badge': '사례 2 · 광고 채널 최적화',
        'results.case2Title': '같은 예산으로 도달 극대화',
        'results.case2Before': 'Google은 트래픽 효율이 가장 낮으면서 예산을 가장 많이 소진했습니다. TikTok은 단가는 저렴했지만 전환이 거의 없었고, Reddit은 타겟팅 정확도가 가장 높아 핵심 유저층에 효과적으로 도달했습니다.',
        'results.case2Strategy': '실시간 비용 데이터를 바탕으로 성과가 가장 높은 채널에 예산을 재배분했습니다 — Reddit 75%, TikTok 25%.',
        'results.case2M1': 'TikTok CPC',
        'results.case2M2': 'Reddit CPC',
        'results.case2M3': 'Google CPV',

        'why.title': '왜 HypePotions인가',
        'why.subtitle': '만드는 일에 집중하고 싶은 인디 개발자를 위한, 스마트하고 유연한 마케팅 파트너입니다.',
        'why.f1Title': '게이머이자 개발자인 마케터',
        'why.f1Desc': '단순한 마케터가 아닙니다. 직접 게임을 개발하고 출시한 경험이 있어 개발자의 언어로 소통합니다.',
        'why.f2Title': '글로벌 네트워크',
        'why.f2Desc': '15개국 이상의 매체·인플루언서·커뮤니티 네트워크 — 첫날부터 게임을 전 세계에 알립니다.',
        'why.f3Title': '데이터 기반 전략',
        'why.f3Desc': 'Steam Analytics와 실시간 캠페인 데이터를 근거로 모든 결정을 내립니다. 감이 아닌 수치로 움직입니다.',
        'why.f4Title': '빠른 실행',
        'why.f4Desc': '3~5 영업일 안에 온보딩을 완료합니다. 출시 일정이 요구하는 속도로 움직입니다.',
        'why.f5Title': '투명한 파트너십',
        'why.f5Desc': '월 정액 하나, 공유 Notion 워크스페이스, 주간 업데이트. 저희가 무엇을 하고 있는지 항상 바로 확인하실 수 있습니다.',
        'why.f6Title': '인디 게임 전문',
        'why.f6Desc': '5년간 20개 이상의 타이틀을 오직 인디 Steam 게임에만 집중해 진행했습니다. 무엇이 통하고 무엇이 통하지 않는지 압니다.',

        'pricing.title': '요금제',
        'pricing.popular': '가장 인기',
        'pricing.plan1Name': 'Starter',
        'pricing.plan1Price': '월 250만원',
        'pricing.plan1Desc': '에이전시 없이 핵심 마케팅부터 시작하는 플랜입니다.',
        'pricing.plan1F1': '✔️ 온라인 페스티벌 신청 & 참가',
        'pricing.plan1F2': '✔️ 보도자료 배포 (월 1회)',
        'pricing.plan1F3': '✔️ Twitter & Reddit 채널 운영',
        'pricing.plan1F4': '✔️ 타겟 오디언스 & 경쟁사 리서치',
        'pricing.plan1F5': '✔️ 전용 Notion 워크스페이스',
        'pricing.plan1F6': '✔️ 월간 성과 리포트',
        'pricing.plan2Name': 'Momentum',
        'pricing.plan2Price': '월 500만원',
        'pricing.plan2Desc': '출시 시점에 전 채널 도달이 필요할 때를 위한 플랜입니다.',
        'pricing.plan2F1': '✔️ Starter의 모든 서비스, 그리고:',
        'pricing.plan2F2': '✔️ TikTok 콘텐츠 전략 & 게시',
        'pricing.plan2F3': '✔️ YouTube 쇼츠 & 클립',
        'pricing.plan2F4': '✔️ 크리에이터 아웃리치',
        'pricing.plan2F5': '✔️ Discord 서버 구축 & 커뮤니티 운영',
        'pricing.plan2F6': '✔️ 온라인 이벤트 지원 (Next Fest·세일 등)',
        'pricing.plan3Name': 'Scale',
        'pricing.plan3Price': '월 800만원',
        'pricing.plan3Desc': '유료 광고·페이지 최적화까지 모두 위탁하는 완전 관리형 플랜입니다.',
        'pricing.plan3F1': '✔️ Momentum의 모든 서비스, 그리고:',
        'pricing.plan3F2': '✔️ 유료 광고 캠페인 셋업 & 최적화',
        'pricing.plan3F3': '✔️ Steam 페이지 최적화',
        'pricing.plan3F4': '✔️ 캡슐 이미지 & 트레일러 피드백',
        'pricing.plan3F5': '✔️ 우선 응답 & 전담 상담',
        'pricing.plan3F6': '✔️ 전담 매니저 & 직통 연결',
        'pricing.note': '유료 보도자료 및 유료 광고의 실제 광고비는 별도 청구됩니다. 부가세 별도.',

        'process.title': '진행 프로세스',
        'process.subtitle': '킥오프부터 결과 리포트까지, 명확하고 반복 가능한 6단계입니다.',
        'process.p1Title': '초기 상담',
        'process.p1Desc': '게임, 목표, 타겟 오디언스를 파악합니다.',
        'process.p2Title': '전략 설계',
        'process.p2Desc': '채널과 시장에 맞는 맞춤형 로드맵을 설계합니다.',
        'process.p3Title': '에셋 제작',
        'process.p3Desc': '전환을 이끄는 콘텐츠·카피·크리에이티브를 제작합니다.',
        'process.p4Title': '캠페인 런칭',
        'process.p4Desc': '언론, 소셜, 광고 채널에 걸쳐 동시에 라이브합니다.',
        'process.p5Title': '모니터링',
        'process.p5Desc': '실시간 성과 데이터를 기반으로 즉시 최적화합니다.',
        'process.p6Title': '리포팅',
        'process.p6Desc': '월간 성과 보고서와 주간 업데이트를 투명하게 공유합니다.',
        'process.note': '평균 온보딩 기간: 3~5 영업일 · 월간 리포트 + 주간 업데이트 · 전담 1:1 매니저',

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
        'faq.a7': '영어가 가능한 한국인과 러시아인으로 구성된 2인 팀입니다. 5인 개발팀의 일원으로 자체 턴제 전략·액션 게임을 개발·출시하며 개발부터 마케팅, 퍼블리싱까지 모두 다뤘습니다. 게임 업계 10년 이상의 경험을 바탕으로 이제 다른 인디 개발자들을 돕고 있습니다.',

        'footer.tagline': '개발에만 집중하세요. 마케팅은 저희가 맡습니다.',
        'footer.ready': '게임을 성장시킬 준비가 되셨나요?',
        'footer.getStarted': '무료 전략 상담 예약하기'
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

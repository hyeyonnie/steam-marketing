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
        'hero.tagline': 'Pause or cancel anytime.',
        'hero.seePricing': 'See Pricing',
        'hero.bookCall': 'Book a Call',

        'logos.text': 'Trusted by indie developers worldwide',

        'stats.title': 'Proof in Numbers',
        'stats.subtitle': 'Five years of Steam marketing, measured in results — not promises.',
        'stats.groupA': 'Our Track Record',
        'stats.titlesPartnered': 'Titles Partnered',
        'stats.globalMarkets': 'Global Markets',
        'stats.avgWishlist': 'Avg. Wishlist Growth',
        'stats.yearsExp': 'Years Experience',
        'stats.groupB': 'Campaign Performance',
        'stats.followerGrowth': 'Avg. Follower Growth',
        'stats.engagement': 'Avg. Post Engagement',
        'stats.prOutlets': 'PR Outlets (11 countries · 7 languages)',
        'stats.bestWishlist': 'Best-Case Wishlist Growth',

        'how.title': 'How it works',
        'how.subtitle': 'Steam marketing, simplified. One flat monthly fee. No surprises.',
        'how.step1Title': 'Subscribe & Share',
        'how.step1Desc': 'Subscribe and get your own Notion page. Share your game details, key milestones, and marketing needs — all in one place.',
        'how.step2Title': 'We Get to Work',
        'how.step2Desc': "We'll build your marketing roadmap: target audience, press, influencer outreach — you can track every step in real-time.",
        'how.step3Title': 'Grow Your Game',
        'how.step3Desc': "More visibility. More wishlists. More players. You focus on development — we'll handle the buzz.",

        'services.title': 'What We Do',
        'services.subtitle': "Four core services that cover your game's entire marketing journey.",
        'services.s1Title': 'Social Media Management',
        'services.s1Desc': 'X, Reddit, TikTok, and YouTube — we build and run your channels and community, driving an average +536% follower growth.',
        'services.s2Title': 'Press Release & PR',
        'services.s2Desc': 'Paid featuring (Famitsu, 4Gamer) and direct distribution to our network — averaging 20+ pickups per title.',
        'services.s3Title': 'Online Event Support',
        'services.s3Desc': 'Steam Next Fest, Steam Sales, and third-party events — we apply, prepare, and maximize every opportunity.',
        'services.s4Title': 'Paid Social Ads',
        'services.s4Desc': 'Reddit, TikTok, and YouTube campaigns, optimized with Steam Analytics for real, measurable wishlist conversion.',
        'services.cta': 'Book a Call',

        'results.title': 'Real Results',
        'results.subtitle': 'How our strategies turned into measurable growth for indie titles.',
        'results.before': 'Before',
        'results.strategy': 'Strategy',
        'results.after': 'After',
        'results.results': 'Results',
        'results.case1Badge': 'Case 1 · Community Strategy',
        'results.case1Title': 'From Wasted Ads to a Thriving Community',
        'results.case1Before': 'Inefficient ad spend, generic tags, and no community presence.',
        'results.case1Strategy': 'Precision targeting, a Reddit-centered community, and Japanese influencer outreach.',
        'results.case1M1': 'Steam Impressions',
        'results.case1M2': 'Page Visits',
        'results.case1M3': 'Wishlists',
        'results.case2Badge': 'Case 2 · Ad Channel Optimization',
        'results.case2Title': 'Squeezing Maximum Reach From Every Dollar',
        'results.case2Strategy': 'Reallocated budget to the highest-performing channels — 75% Reddit, 25% TikTok — based on live cost data.',
        'results.case2M1': 'TikTok CPC',
        'results.case2M2': 'Reddit CPC',
        'results.case2M3': 'Google CPV',

        'pr.title': 'Global PR Network',
        'pr.subtitle': 'Your game, in front of the right press — across the world.',
        'pr.outlets': 'Media Outlets',
        'pr.countries': 'Countries',
        'pr.languages': 'Languages',
        'pr.featuredLabel': 'Featured outlets include',
        'pr.regionsLabel': 'Coverage across',

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

        'testimonials.title': 'What Our Partners Say',
        'testimonials.t1': '“I was struggling with getting visibility outside Korea, and they helped us connect with creators and update our Steam page. As a result, we saw a big jump in wishlists during a major festival.”',
        'testimonials.a1': '— Pocket Legend Dev Team',
        'testimonials.t2': "“The team's expertise in Steam's ecosystem is unmatched. They helped us optimize our store page and run a successful festival campaign, leading to a 200% increase in daily wishlists.”",
        'testimonials.a2': '— IndieGame Corp.',

        'pricing.title': 'Plans',
        'pricing.starterDesc': 'Your first step on the marketing quest',
        'pricing.getStarted': 'Get Started',
        'pricing.starterF1': '✔️ Target audience research',
        'pricing.starterF2': '✔️ Steam page optimization',
        'pricing.starterF3': '✔️ Online festival applications & participation',
        'pricing.starterF4': '✔️ Content creator outreach',
        'pricing.starterF5': '✔️ Press release',
        'pricing.starterF6': '✔️ Twitter & Reddit post management',
        'pricing.popular': 'Most Popular',
        'pricing.proDesc': 'Starter gets you going. Pro brings full-channel growth.',
        'pricing.proF1': '✔️ Everything in Starter, plus:',
        'pricing.proF2': '✔️ TikTok content strategy & posting',
        'pricing.proF3': '✔️ YouTube shorts & clips',
        'pricing.proF4': '✔️ Discord setup & community management',
        'pricing.proF5': '✔️ Paid ad campaign setup, management, and optimization',
        'pricing.revShareTitle': 'Revenue Share',
        'pricing.custom': 'Custom',
        'pricing.revShareDesc': "Prefer a revenue share model instead of a monthly fee? We're open to that too. Let's chat and see if it's a good fit - just reach out!",
        'pricing.submitGame': 'Submit Your Game',

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
        'faq.q3': 'Is there a trial period?',
        'faq.a3': "Not officially, but if you're not satisfied after the first month, we'll offer a 50% refund — no hard feelings.",
        'faq.q4': 'Do you manage paid ads?',
        'faq.a4': 'Yes. Once we align on campaign goals and budget, we handle setup, optimization, and management.',
        'faq.q5': 'Do you create trailers?',
        'faq.a5': 'We create short-form videos for social media and Steam updates. For cinematic trailers, we recommend working with a specialized studio.',
        'faq.q6': 'Do you only work with Steam games? What about mobile?',
        'faq.a6': 'We specialize in PC/Steam games. At this time, we do not support mobile game marketing.',
        'faq.q7': 'Do you offer funding for revenue share projects?',
        'faq.a7': "Yes — we can invest up to $50,000 in select titles under our revenue share model. If you're interested, submit your game for review.",
        'faq.q8': 'What if I only have a few marketing needs right now?',
        'faq.a8': "No problem. You can sign up, make your requests, then pause or cancel your plan anytime. Come back when you're ready for more support — we're flexible.",
        'faq.q9': 'How do I communicate and track progress?',
        'faq.a9': "Once you sign up, you'll get access to a dedicated Notion page. There, you can share info, track tasks, view updates, and communicate directly with us — all in one place.",
        'faq.q10': "Who's behind this service?",
        'faq.a10': "We're a two-person team — one from Korea and one from Russia — both fluent in English. As part of a 5-person dev team, we've built and launched our own turn-based strategy and action games, handling everything from development to marketing and publishing. With over 10 years in the game industry, we now help other indie devs do the same.",

        'footer.tagline': 'Focus on development. We handle the marketing.',
        'footer.ready': 'Ready to grow your game?',
        'footer.getStarted': 'Get Started Today'
    },
    ko: {
        'nav.proof': '실적',
        'nav.services': '서비스',
        'nav.benefits': '강점',
        'nav.pricing': '가격',
        'nav.bookCall': '상담 예약',

        'hero.title': '마케팅에 쓸 100시간을 아끼세요',
        'hero.subtitle': '당신이 사랑하는 게임 개발에 집중하세요. 마케팅은 저희가 맡습니다.',
        'hero.tagline': '언제든 일시정지하거나 해지할 수 있습니다.',
        'hero.seePricing': '가격 보기',
        'hero.bookCall': '상담 예약',

        'logos.text': '전 세계 인디 개발자들이 신뢰합니다',

        'stats.title': '숫자로 증명합니다',
        'stats.subtitle': '약속이 아닌 결과로 증명한 5년간의 스팀 마케팅.',
        'stats.groupA': '우리의 실적',
        'stats.titlesPartnered': '파트너 타이틀',
        'stats.globalMarkets': '글로벌 마켓',
        'stats.avgWishlist': '평균 위시리스트 증가',
        'stats.yearsExp': '스팀 마케팅 경력',
        'stats.groupB': '캠페인 성과',
        'stats.followerGrowth': '팔로워 평균 성장률',
        'stats.engagement': '게시물 평균 인게이지먼트',
        'stats.prOutlets': 'PR 매체 (11개국 · 7개 언어)',
        'stats.bestWishlist': '최고 위시리스트 증가 실적',

        'how.title': '진행 방식',
        'how.subtitle': '간단해진 스팀 마케팅. 월 정액 하나로. 숨은 비용 없이.',
        'how.step1Title': '구독하고 공유하기',
        'how.step1Desc': '구독하면 전용 노션 페이지가 제공됩니다. 게임 정보, 주요 마일스톤, 마케팅 니즈를 한곳에서 공유하세요.',
        'how.step2Title': '저희가 작업합니다',
        'how.step2Desc': '타겟 오디언스, 언론, 인플루언서 아웃리치까지 마케팅 로드맵을 설계하고, 모든 단계를 실시간으로 확인할 수 있습니다.',
        'how.step3Title': '게임을 성장시키기',
        'how.step3Desc': '더 많은 노출, 더 많은 위시리스트, 더 많은 플레이어. 개발에 집중하세요 — 화제는 저희가 만듭니다.',

        'services.title': '제공 서비스',
        'services.subtitle': '게임 마케팅의 전 여정을 아우르는 4대 핵심 서비스.',
        'services.s1Title': '소셜 미디어 운영',
        'services.s1Desc': 'X, Reddit, TikTok, YouTube 채널과 커뮤니티를 구축·운영하여 평균 +536% 팔로워 성장을 이끕니다.',
        'services.s2Title': '보도자료 & PR',
        'services.s2Desc': '유료 피처링(Famitsu, 4Gamer)과 자체 네트워크 직접 배포로 타이틀당 평균 20회 이상의 노출을 만듭니다.',
        'services.s3Title': '온라인 이벤트 지원',
        'services.s3Desc': 'Steam Next Fest, Steam 세일, 서드파티 이벤트까지 — 신청·준비·활용을 모두 극대화합니다.',
        'services.s4Title': '유료 소셜 광고',
        'services.s4Desc': 'Reddit, TikTok, YouTube 캠페인을 Steam Analytics와 연동해 실질적이고 측정 가능한 위시리스트 전환으로 최적화합니다.',
        'services.cta': '상담 예약',

        'results.title': '실제 성과',
        'results.subtitle': '우리의 전략이 인디 타이틀의 측정 가능한 성장으로 이어진 사례.',
        'results.before': 'Before',
        'results.strategy': '전략',
        'results.after': 'After',
        'results.results': '결과',
        'results.case1Badge': '사례 1 · 커뮤니티 전략',
        'results.case1Title': '낭비되던 광고에서 살아있는 커뮤니티로',
        'results.case1Before': '비효율적인 광고비, 범용 태그, 커뮤니티 부재.',
        'results.case1Strategy': '정밀 타겟팅, Reddit 중심 커뮤니티, 일본 인플루언서 아웃리치.',
        'results.case1M1': 'Steam 노출',
        'results.case1M2': '페이지 방문',
        'results.case1M3': '위시리스트',
        'results.case2Badge': '사례 2 · 광고 채널 최적화',
        'results.case2Title': '한 푼까지 최대 도달로 짜내기',
        'results.case2Strategy': '실시간 비용 데이터를 기반으로 성과가 가장 높은 채널에 예산을 재배분 — Reddit 75%, TikTok 25%.',
        'results.case2M1': 'TikTok CPC',
        'results.case2M2': 'Reddit CPC',
        'results.case2M3': 'Google CPV',

        'pr.title': '글로벌 PR 네트워크',
        'pr.subtitle': '당신의 게임을, 전 세계의 알맞은 매체 앞에.',
        'pr.outlets': '매체',
        'pr.countries': '개국',
        'pr.languages': '개 언어',
        'pr.featuredLabel': '주요 매체',
        'pr.regionsLabel': '커버리지 권역',

        'why.title': '우리를 선택하는 이유',
        'why.subtitle': '직접 뛰기보다 만들기에 집중하고 싶은 인디 개발자를 위한 스마트하고 유연한 마케팅.',
        'why.f1Title': '게이머이자 개발자인 마케터',
        'why.f1Desc': '단순한 마케터가 아닙니다 — 직접 게임을 출시한 게이머이자 개발자입니다. 우리는 같은 언어를 씁니다.',
        'why.f2Title': '글로벌 네트워크',
        'why.f2Desc': '15개국 이상의 매체·인플루언서·커뮤니티 도달 — 첫날부터 당신의 게임을 전 세계로.',
        'why.f3Title': '데이터 기반 전략',
        'why.f3Desc': '모든 결정은 Steam Analytics와 실시간 캠페인 데이터에 근거합니다 — 추측이 아닌 결과.',
        'why.f4Title': '빠른 실행',
        'why.f4Desc': '3~5 영업일 내 온보딩. 출시 일정이 요구하는 속도로 움직입니다.',
        'why.f5Title': '투명한 파트너십',
        'why.f5Desc': '월 정액 하나, 공유 노션 HQ, 주간 업데이트. 우리가 무엇을 하는지 항상 정확히 아실 수 있습니다.',
        'why.f6Title': '인디 특화 경험',
        'why.f6Desc': '5년간 20개 이상의 타이틀, 오직 인디 스팀 게임에만 집중 — 무엇이 통하고 무엇이 안 통하는지 압니다.',

        'testimonials.title': '파트너들의 후기',
        'testimonials.t1': '“한국 밖에서의 노출 확보에 어려움을 겪고 있었는데, 크리에이터 연결과 스팀 페이지 개선을 도와주셨어요. 그 결과 대형 페스티벌 기간에 위시리스트가 크게 늘었습니다.”',
        'testimonials.a1': '— Pocket Legend 개발팀',
        'testimonials.t2': '“스팀 생태계에 대한 팀의 전문성은 타의 추종을 불허합니다. 스토어 페이지 최적화와 성공적인 페스티벌 캠페인을 도와주셔서 일일 위시리스트가 200% 증가했습니다.”',
        'testimonials.a2': '— IndieGame Corp.',

        'pricing.title': '요금제',
        'pricing.starterDesc': '마케팅 퀘스트의 첫걸음',
        'pricing.getStarted': '시작하기',
        'pricing.starterF1': '✔️ 타겟 오디언스 리서치',
        'pricing.starterF2': '✔️ 스팀 페이지 최적화',
        'pricing.starterF3': '✔️ 온라인 페스티벌 신청 & 참가',
        'pricing.starterF4': '✔️ 콘텐츠 크리에이터 아웃리치',
        'pricing.starterF5': '✔️ 보도자료',
        'pricing.starterF6': '✔️ Twitter & Reddit 게시물 운영',
        'pricing.popular': '가장 인기',
        'pricing.proDesc': 'Starter로 출발하고, Pro로 전 채널 성장을.',
        'pricing.proF1': '✔️ Starter의 모든 것, 그리고:',
        'pricing.proF2': '✔️ TikTok 콘텐츠 전략 & 게시',
        'pricing.proF3': '✔️ YouTube 쇼츠 & 클립',
        'pricing.proF4': '✔️ Discord 구축 & 커뮤니티 운영',
        'pricing.proF5': '✔️ 유료 광고 캠페인 설정·운영·최적화',
        'pricing.revShareTitle': '수익 배분',
        'pricing.custom': '맞춤형',
        'pricing.revShareDesc': '월 정액 대신 수익 배분 모델을 선호하시나요? 저희도 열려 있습니다. 잘 맞을지 함께 이야기해봐요 — 편하게 연락 주세요!',
        'pricing.submitGame': '게임 제출하기',

        'process.title': '진행 프로세스',
        'process.subtitle': '킥오프부터 결과까지, 명확하고 반복 가능한 경로.',
        'process.p1Title': '초기 상담',
        'process.p1Desc': '게임, 목표, 오디언스를 파악합니다.',
        'process.p2Title': '전략 설계',
        'process.p2Desc': '채널과 마켓 전반의 맞춤형 로드맵.',
        'process.p3Title': '에셋 제작',
        'process.p3Desc': '전환을 위한 콘텐츠·카피·크리에이티브 제작.',
        'process.p4Title': '캠페인 런칭',
        'process.p4Desc': '언론, 소셜, 광고에 걸쳐 라이브로 진행합니다.',
        'process.p5Title': '모니터링',
        'process.p5Desc': '실제 성과 데이터를 기반으로 실시간 최적화.',
        'process.p6Title': '리포팅',
        'process.p6Desc': '월간 리포트와 주간 업데이트, 언제나 투명하게.',
        'process.note': '평균 온보딩: 3~5 영업일 · 월간 리포트 + 주간 업데이트 · 전담 매니저 1:1',

        'faq.title': '자주 묻는 질문',
        'faq.q1': '이미 스팀 페이지가 있어야 하나요?',
        'faq.a1': '네, 또는 첫 달에 저희와 함께 페이지를 오픈할 준비가 되어 있어야 합니다.',
        'faq.q2': '게임 데모를 공유해야 하나요?',
        'faq.a2': '네 — 게임을 이해하고 효과적으로 콘텐츠를 만들려면 플레이 가능한 빌드에 접근할 수 있어야 합니다.',
        'faq.q3': '체험 기간이 있나요?',
        'faq.a3': '공식적으로는 없지만, 첫 달 후 만족하지 못하시면 50% 환불을 제공합니다 — 서운함 없이요.',
        'faq.q4': '유료 광고도 운영하나요?',
        'faq.a4': '네. 캠페인 목표와 예산을 함께 정하면 설정, 최적화, 운영까지 모두 진행합니다.',
        'faq.q5': '트레일러도 제작하나요?',
        'faq.a5': '소셜 미디어와 스팀 업데이트용 숏폼 영상을 제작합니다. 시네마틱 트레일러는 전문 스튜디오와 협업하시길 권합니다.',
        'faq.q6': '스팀 게임만 작업하나요? 모바일은요?',
        'faq.a6': '저희는 PC/스팀 게임에 특화되어 있습니다. 현재 모바일 게임 마케팅은 지원하지 않습니다.',
        'faq.q7': '수익 배분 프로젝트에 투자도 하나요?',
        'faq.a7': '네 — 수익 배분 모델 하에 선정된 타이틀에 최대 $50,000까지 투자할 수 있습니다. 관심 있으시면 게임을 제출해 검토받으세요.',
        'faq.q8': '지금은 마케팅 니즈가 몇 가지뿐인데 괜찮을까요?',
        'faq.a8': '문제없습니다. 가입 후 필요한 것을 요청하고, 언제든 일시정지하거나 해지할 수 있습니다. 더 많은 지원이 필요할 때 다시 오세요 — 유연하게 운영합니다.',
        'faq.q9': '어떻게 소통하고 진행 상황을 확인하나요?',
        'faq.a9': '가입하시면 전용 노션 페이지에 접근할 수 있습니다. 그곳에서 정보 공유, 작업 추적, 업데이트 확인, 직접 소통까지 한곳에서 가능합니다.',
        'faq.q10': '이 서비스는 누가 운영하나요?',
        'faq.a10': '한국과 러시아 출신, 영어에 능통한 2인 팀입니다. 5인 개발팀의 일원으로 자체 턴제 전략·액션 게임을 개발·출시하며 개발부터 마케팅, 퍼블리싱까지 모두 다뤘습니다. 게임 업계 10년 이상의 경험으로 이제 다른 인디 개발자들을 돕습니다.',

        'footer.tagline': '개발에 집중하세요. 마케팅은 저희가 맡습니다.',
        'footer.ready': '게임을 성장시킬 준비가 되셨나요?',
        'footer.getStarted': '지금 시작하기'
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

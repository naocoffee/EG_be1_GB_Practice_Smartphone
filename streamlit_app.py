import streamlit as st
import random

# ============================================================
# ページ設定
# ============================================================
st.set_page_config(
    page_title="Tense Mastery Test",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ============================================================
# クイズデータ（Lesson 3〜5 厳選5問）
# ============================================================
QUESTIONS = [
    {
        "id": 1,
        "lesson": "Lesson 3 (未来表現)",
        "question": "We will leave home as soon as you (      ) ready.",
        "options": ["will be", "are", "have been", "were"],
        "answer": "are",
        "translation": "あなたの準備ができ次第、私たちは家を出発します。",
        "explanation": "「as soon as（〜するとすぐに）」は『時』を表す副詞節をつくる接続詞です。when・after・before・until・by the time・next timeなど『時』を表す接続詞の節の中では、未来のことを表す場合でも動詞は現在形を使います（× will be としない）。同様に、if などの『条件』を表す節でも未来のことは現在形で表します。",
        "ref": "ClearGB Lesson 3-C「when や if のあとの現在形」（教科書 pp.090-093）",
    },
    {
        "id": 2,
        "lesson": "Lesson 3 (未来完了形)",
        "question": "By the end of the month, I (      ) all the books on my list.",
        "options": ["read", "have read", "have been read", "will have read"],
        "answer": "will have read",
        "translation": "今月末までに、私はリストにある本をすべて読み終えているだろう。",
        "explanation": "「By the end of the month（今月の終わりまでに）」という未来の特定の時点までに完了している動作を表すため、未来完了形『will have ＋ 過去分詞』を使用します。未来完了形は、未来のある時点で「完了しているであろうこと」や「継続しているであろうこと」を表すときに使います。",
        "ref": "ClearGB Lesson 5-C「未来完了形〈will have＋過去分詞〉」（教科書 pp.117-119）",
    },
    {
        "id": 3,
        "lesson": "Lesson 4 (現在完了進行形)",
        "question": "He (      ) karaoke for a few hours.",
        "options": ["is singing", "has been singing", "sang", "had been singing"],
        "answer": "has been singing",
        "translation": "彼は数時間（ずっと）カラオケを歌い続けている。",
        "explanation": "「数時間（ずっと）カラオケを歌い続けている」という、過去に始まった動作が現在も途切れずに続いている状態を表すため、現在完了進行形『have/has been ＋ 動詞の-ing形』を使用します。「ずっと続いている動作」はこのように動作動詞の現在完了進行形で表すのが基本です。",
        "ref": "ClearGB Lesson 4-C「現在完了形・現在完了進行形：継続」（教科書 pp.108-110）",
    },
    {
        "id": 4,
        "lesson": "Lesson 5 (過去完了/大過去)",
        "question": "Ann knew that I (      ) my smartphone the day before.",
        "options": ["lose", "lost", "have lost", "had lost"],
        "answer": "had lost",
        "translation": "アンは、私が前日にスマートフォンをなくしていたことを知っていた。",
        "explanation": "「アンが知っていた（knew：過去形）」よりも前の時間（前日）に「私がスマホをなくした」という関係です。このように「過去のある時点から見た、さらなる過去」のことを『大過去』と呼び、過去完了形『had ＋ 過去分詞』で表します。過去完了形は、基準となる『過去のある時点』がいつなのかがはっきりしている必要があります。",
        "ref": "ClearGB Lesson 5-A「過去完了形：完了・経験・大過去」（教科書 pp.116-117）",
    },
    {
        "id": 5,
        "lesson": "Lesson 5 (過去完了/完了・結果)",
        "question": "Ken (      ) just (      ) home when I called him.",
        "options": ["has, come", "had, come", "is, coming", "will, come"],
        "answer": "had, come",
        "translation": "私が電話をかけたとき、ケンはちょうど帰宅したところだった。",
        "explanation": "私が電話した時点（when I called him：過去形）で、ケンはすでに帰宅し終わっていたという、過去のある時点での完了状態を表します。just（ちょうど）とともに用いて、過去完了形『had ＋ just ＋ 過去分詞』で「ちょうど～し終えていた」を表現します。",
        "ref": "ClearGB Lesson 5-A「過去完了形：完了・経験・大過去」（教科書 pp.112-114）",
    },
]

TOTAL_QUESTIONS = 10

# ============================================================
# CSS
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

    .stApp {
        background: #f0eee9;
        color: #33312e;
    }

    section.main > div {
        padding-top: 0.5rem;
    }

    * {
        font-family: 'Space Grotesk', sans-serif;
    }

    h1, h2, h3 {
        color: #33312e;
        font-weight: 600;
    }

    .app-title {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 700;
        color: #33312e;
        letter-spacing: 0.5px;
        margin-bottom: 0;
    }
    .app-subtitle {
        text-align: center;
        font-size: 0.8rem;
        color: #8c887f;
        margin-bottom: 1rem;
        letter-spacing: 1px;
    }

    /* ---- 進捗バー ---- */
    .progress-label {
        text-align: center;
        color: #96917f;
        letter-spacing: 1px;
        margin-bottom: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    .progress-bar-outer {
        width: 100%;
        height: 8px;
        background: #d8d4c8;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 6px;
    }
    .progress-bar-inner {
        height: 100%;
        background: #2f8fb8;
        border-radius: 4px;
        transition: width 0.4s ease-in-out;
    }
    .score-tag {
        text-align: center;
        font-size: 0.82rem;
        color: #6f6b62;
        margin-bottom: 14px;
    }

    /* ---- 問題エリア ---- */
    .question-card {
        background: #e7e4dc;
        border: 1px solid #d8d4c8;
        border-radius: 10px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }
    .lesson-tag {
        display: inline-block;
        background: #fdf0d0;
        color: #a97c0a;
        font-weight: 600;
        font-size: 0.68rem;
        padding: 2px 9px;
        border-radius: 20px;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }
    .question-text {
        font-size: 1.15rem;
        font-weight: 600;
        color: #33312e;
        line-height: 1.5;
    }

    /* ---- 判定表示 ---- */
    .effect-text {
        text-align: center;
        font-size: 0.95rem;
        font-weight: 700;
        padding: 10px;
        margin: 10px 0 8px 0;
        border-radius: 8px;
    }
    .effect-win {
        color: #17a86b;
        background: #17a86b14;
        border: 1px solid #17a86b40;
    }
    .effect-lose {
        color: #d6394a;
        background: #d6394a14;
        border: 1px solid #d6394a40;
    }

    .explain-box {
        background: #e7e4dc;
        border-left: 3px solid #c48f10;
        border-radius: 6px;
        padding: 10px 14px;
        margin-top: 6px;
        font-size: 0.92rem;
        line-height: 1.6;
        color: #4a473f;
    }
    .explain-title {
        font-size: 0.68rem;
        font-weight: 700;
        color: #b5860a;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .ref-note {
        font-size: 0.76rem;
        color: #8c887f;
        margin-top: 6px;
        padding-top: 6px;
        border-top: 1px dashed #d8d4c8;
    }
    .translation-line {
        font-size: 0.88rem;
        color: #5a574c;
        margin: 4px 0 8px 0;
        font-style: italic;
    }
    .translation-line.plain {
        font-style: normal;
    }

    /* ---- 選択肢（ラジオボタン） ---- */
    div[data-testid="stRadio"] label p {
        font-size: 1.2rem !important;
        font-weight: 600;
        color: #33312e;
    }
    div[data-testid="stRadio"] label {
        padding: 6px 0;
    }

    /* ---- ボタン ---- */
    div.stButton > button {
        font-weight: 600;
        font-size: 0.95rem;
        background: #e7e4dc;
        color: #33312e;
        border: 1px solid #d0ccc0;
        border-radius: 8px;
        padding: 6px 4px;
        width: 100%;
        transition: all 0.15s ease-in-out;
    }
    div.stButton > button:hover {
        background: #ddd8cb;
        border-color: #c48f10;
        color: #93690b;
    }
    div.stButton > button:active {
        transform: translateY(1px);
    }

    /* 決定ボタン強調 */
    .decide-btn button {
        background: #2f8fb8 !important;
        border-color: #2f8fb8 !important;
        color: #ffffff !important;
    }
    .decide-btn button:hover {
        background: #26759a !important;
        color: #ffffff !important;
    }

    /* ---- 結果画面 ---- */
    .result-title {
        text-align: center;
        font-size: 1.7rem;
        font-weight: 700;
        margin: 6px 0 4px 0;
        color: #33312e;
    }
    .result-score {
        text-align: center;
        font-size: 1.0rem;
        color: #6f6b62;
        margin-bottom: 16px;
    }

    .weakpoint-card {
        background: #e7e4dc;
        border: 1px solid #d8d4c8;
        border-left: 3px solid #d6394a;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 10px;
    }
    .weakpoint-q {
        font-weight: 600;
        font-size: 1.0rem;
        color: #33312e;
        margin-bottom: 4px;
    }
    .weakpoint-ans {
        font-size: 0.88rem;
        color: #17a86b;
        margin-bottom: 4px;
    }

    .badge-correct {
        display:inline-block;
        background:#17a86b14;
        color:#17a86b;
        border:1px solid #17a86b40;
        border-radius:20px;
        padding:1px 10px;
        font-weight:600;
        font-size:0.78rem;
        margin-bottom:6px;
    }
    .badge-wrong {
        display:inline-block;
        background:#d6394a14;
        color:#d6394a;
        border:1px solid #d6394a40;
        border-radius:20px;
        padding:1px 10px;
        font-weight:600;
        font-size:0.78rem;
        margin-bottom:6px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# セッション状態の初期化
# ============================================================
def init_state():
    order = []
    while len(order) < TOTAL_QUESTIONS:
        batch = list(range(len(QUESTIONS)))
        random.shuffle(batch)
        order.extend(batch)
    order = order[:TOTAL_QUESTIONS]
    st.session_state.order = order
    st.session_state.current_index = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.test_over = False
    st.session_state.correct_count = 0
    st.session_state.weak_points = []
    st.session_state.last_correct = None


if "order" not in st.session_state:
    init_state()


# ============================================================
# ヘルパー関数
# ============================================================
def render_progress_bar(current, total):
    pct = int(100 * current / total)
    return f"""
    <div class="progress-bar-outer">
        <div class="progress-bar-inner" style="width:{pct}%;"></div>
    </div>
    """


def go_next_question():
    st.session_state.current_index += 1
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.last_correct = None
    if st.session_state.current_index >= TOTAL_QUESTIONS:
        st.session_state.test_over = True


def submit_answer(q, chosen):
    st.session_state.selected_option = chosen
    st.session_state.answered = True
    is_correct = chosen == q["answer"]
    st.session_state.last_correct = is_correct
    if is_correct:
        st.session_state.correct_count += 1
    else:
        st.session_state.weak_points.append(
            {
                "question": q["question"],
                "answer": q["answer"],
                "explanation": q["explanation"],
                "ref": q["ref"],
                "translation": q["translation"],
                "lesson": q["lesson"],
                "chosen": chosen,
            }
        )


# ============================================================
# ヘッダー
# ============================================================
st.markdown('<div class="app-title">📝 TENSE MASTERY TEST</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">— 時制 10問テスト —</div>', unsafe_allow_html=True)

# ============================================================
# 結果画面
# ============================================================
if st.session_state.test_over:
    correct_count = st.session_state.correct_count
    wrong_count = len(st.session_state.weak_points)

    st.markdown('<div class="result-title">🏁 テスト終了！</div>', unsafe_allow_html=True)
    st.markdown(
        f"<div class='result-score'>{TOTAL_QUESTIONS}問中 "
        f"<span style='color:#17a86b; font-weight:700;'>{correct_count}問正解</span>"
        f" / <span style='color:#d6394a; font-weight:700;'>{wrong_count}問不正解</span></div>",
        unsafe_allow_html=True,
    )

    if st.session_state.weak_points:
        st.markdown(
            "<div style='font-size:0.95rem; font-weight:600; color:#33312e; margin-bottom:2px;'>"
            "📖 今回の弱点（お守りブック）</div>"
            "<div style='color:#8c887f; font-size:0.82rem; margin-bottom:10px;'>"
            "間違えた問題をもう一度確認しよう</div>",
            unsafe_allow_html=True,
        )
        for i, wp in enumerate(st.session_state.weak_points, start=1):
            st.markdown(
                f"""
                <div class="weakpoint-card">
                    <span class="lesson-tag">{wp['lesson']}</span>
                    <div class="weakpoint-q">Q{i}. {wp['question']}</div>
                    <div class="translation-line">🇯🇵 {wp['translation']}</div>
                    <div style="color:#c0405a; font-size:0.85rem; margin-bottom:4px;">
                        あなたの解答: {wp['chosen']}
                    </div>
                    <div class="weakpoint-ans">✅ 正解: {wp['answer']}</div>
                    <div class="explain-box">
                        <div class="explain-title">📝 文法解説</div>
                        {wp['explanation']}
                        <div class="ref-note">📚 参照: {wp['ref']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.markdown(
            "<div style='text-align:center; font-size:1.0rem; font-weight:600; "
            "color:#17a86b; margin:6px 0 14px 0;'>🎉 全問正解！お守りブックは空っぽです</div>",
            unsafe_allow_html=True,
        )

    if st.button("🔄 もう一度挑戦する", use_container_width=True):
        init_state()
        st.rerun()

# ============================================================
# 出題画面
# ============================================================
else:
    q_idx = st.session_state.order[st.session_state.current_index]
    q = QUESTIONS[q_idx]

    st.markdown(
        f'<div class="progress-label">Q{st.session_state.current_index + 1} / {TOTAL_QUESTIONS}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        render_progress_bar(st.session_state.current_index, TOTAL_QUESTIONS),
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div class='score-tag'>現在の正解数: "
        f"<b style='color:#17a86b;'>{st.session_state.correct_count}</b> / "
        f"{st.session_state.current_index}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="question-card">
            <span class="lesson-tag">{q['lesson']}</span>
            <div class="question-text">{q['question']}</div>
            <div class="translation-line plain">🇯🇵 {q['translation']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.answered:
        choice = st.radio(
            "選択肢を選んでください",
            q["options"],
            key=f"radio_{st.session_state.current_index}",
            label_visibility="collapsed",
        )
        st.markdown('<div class="decide-btn">', unsafe_allow_html=True)
        if st.button("✅ 決定 (ANSWER)", use_container_width=True):
            submit_answer(q, choice)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        is_correct = st.session_state.last_correct
        effect_class = "effect-win" if is_correct else "effect-lose"
        result_label = "◎ CORRECT!" if is_correct else "× INCORRECT..."
        st.markdown(
            f'<div class="effect-text {effect_class}">{result_label}</div>',
            unsafe_allow_html=True,
        )

        badge_class = "badge-correct" if is_correct else "badge-wrong"
        badge_text = "正解" if is_correct else "不正解"
        st.markdown(f'<span class="{badge_class}">{badge_text}</span>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="translation-line">🇯🇵 {q['translation']}</div>
            <div style="font-size:0.9rem; color:#4a473f; margin:6px 0 8px 0;">
                あなたの解答: <b>{st.session_state.selected_option}</b> ／ 正解: <b style="color:#17a86b;">{q['answer']}</b>
            </div>
            <div class="explain-box">
                <div class="explain-title">日本語文法解説</div>
                {q['explanation']}
                <div class="ref-note">📚 参照: {q['ref']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        is_last = st.session_state.current_index + 1 >= TOTAL_QUESTIONS
        btn_label = "🏁 結果を見る (Finish)" if is_last else "▶ 次の問題へ (Next Question)"

        if st.button(btn_label, use_container_width=True):
            go_next_question()
            st.rerun()
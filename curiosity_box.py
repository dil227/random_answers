import streamlit as st

st.set_page_config(
    page_title="Curiosity Box",
    layout="centered"
)

st.title("Just answer to see the results and proceed to next stage")

# --------------------------------------------------
# CONTENT
# --------------------------------------------------

MAIN_QUESTIONS = [
    "کیا آپ انجانی چیزوں سے ڈرنے کے بجائے انہیں جاننے کی کوشش کرتے ہیں؟",
    "جب دل بالکل نہ چاہ رہا ہو، کیا پھر بھی آپ اپنے طے کیے ہوئے کام پر قائم رہتے ہیں؟",
    "اگر آپ کافی دیر اکیلے رہیں، تو کیا آپ کا دل کسی انسان کی صحبت چاہنے لگتا ہے؟",
    "بحث میں آپ کے لیے زیادہ اہم کیا ہے: سامنے والے کو سمجھنا یا اپنی بات منوانا؟",
    "جب مستقبل غیر یقینی ہو، تو کیا آپ کا ذہن خود بخود بدترین امکانات سوچنے لگتا ہے؟",
]

METACOGNITION_QUESTIONS = [
    "جب سب کچھ پلان کے خلاف جا رہا ہو، آپ صبر کرتے ہیں یا سسٹم کریش؟ 😅",
    "جو بدل سکتے ہیں، بدلتے ہیں یا پوری کائنات کو قصوروار ٹھہراتے ہیں؟",
    "مشکل وقت میں آپ اپنے اصولوں پر قائم رہتے ہیں یا اصول بھی mood کے ساتھ بدل جاتے ہیں؟",
    "جب سمجھ نہ آئے آگے کیا ہوگا، بھروسہ باقی رہتا ہے یا overthinking شروع؟",
    "فیصلہ کرتے وقت عقل آگے چلتی ہے یا جذبات پہلے پہنچ جاتے ہیں؟",
]

TEXT_SCORE4 = (
    "Let's learn something new — wal-'asr, inal insana lafi khusr (Quran).\n\n"
    "What do you think about it?"
)

TEXT_LOW_SUBSCORE = """صبر:
جب نتیجہ آپ کے حق میں نہ ہو، کیا آپ صبر کے ساتھ صحیح راستے پر قائم رہ سکتے ہیں؟

11:88 — اپنی استطاعت کے مطابق اصلاح:
کیا آپ اُن چیزوں کو بدلنے کی کوشش کرتے ہیں جو آپ کے اختیار میں ہیں، اور باقی اللہ پر چھوڑ دیتے ہیں؟

11:112–115 — ثابت قدمی:
مشکل وقت میں کیا آپ نماز، نیکی اور صبر کے ذریعے خود کو سنبھالنے کی کوشش کرتے ہیں؟

11:123 — عبادت اور توکل:
جب آپ کو آگے کا راستہ نظر نہ آئے، کیا آپ اللہ پر بھروسہ رکھ سکتے ہیں؟

12:5–6 — حکمت:
کیا آپ مشکل حالات میں فوراً ردِعمل دینے کے بجائے سوچ سمجھ کر قدم اٹھاتے ہیں؟"""

TEXT_HIGH_SUBSCORE = """12:18 — صبرِ جمیل:
جب کوئی ایسی بات ہو جسے آپ بدل نہیں سکتے، کیا آپ شکایت کے بجائے صبر اختیار کر سکتے ہیں؟

12:23 — آزمائش:
جب کوئی خواہش آپ کو غلط سمت لے جا رہی ہو، کیا آپ اللہ کی پناہ مانگ کر خود کو روک سکتے ہیں؟

12:33 — صحیح راستہ بمقابلہ آسان راستہ:
اگر صحیح کام مشکل اور غلط کام آسان ہو، تو کیا آپ پھر بھی صحیح راستہ چنتے ہیں؟

13:11 — تبدیلی:
جب زندگی میں تبدیلی کی ضرورت ہو، کیا آپ دوسروں کو بدلنے سے پہلے اپنے اندر تبدیلی لانے کی کوشش کرتے ہیں؟ 👀"""

TEXT_CAVE_REFLECTION = """Faith under pressure — People of the Cave: 18:9–26
"If Allah wills" when planning: 18:23–24
Wealth is temporary — Two Gardens: 18:32–44, especially 18:45–46
Hidden wisdom / limits of perception — Musa & Khidr: 18:60–82, especially 18:68, 18:78–82
Patience before judgment: 18:67–70
Power as responsibility — Dhul-Qarnayn: 18:83–98, especially 18:87–88, 18:94–98
Knowledge must become righteous action: 18:30, 18:107–108
Human knowledge is limited: 18:68, 18:109
Life itself is a test: 18:7
Return to Allah: 18:110 — "Whoever hopes for the meeting with their Lord, let them do righteous deeds…\""""

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "step" not in st.session_state:
    st.session_state.step = "main"          # main -> branch -> sub_quiz -> end
if "main_score" not in st.session_state:
    st.session_state.main_score = 0
if "sub_score" not in st.session_state:
    st.session_state.sub_score = None
if "control_choice" not in st.session_state:
    st.session_state.control_choice = None

# --------------------------------------------------
# STEP 1: MAIN QUESTIONS
# --------------------------------------------------

if st.session_state.step == "main":

    st.caption(f"Questions 1–{len(MAIN_QUESTIONS)}")

    with st.form("main_form"):
        current_answers = []
        for i, question in enumerate(MAIN_QUESTIONS):
            answer = st.radio(
                question,
                ["ہاں", "نہیں"],
                key=f"main_q_{i}",
                horizontal=True,
            )
            current_answers.append(answer)

        submitted = st.form_submit_button("Explore")

    if submitted:
        st.session_state.main_score = sum(a == "ہاں" for a in current_answers)
        st.session_state.step = "branch"
        st.rerun()

# --------------------------------------------------
# STEP 2: BRANCH BASED ON MAIN SCORE
# --------------------------------------------------

elif st.session_state.step == "branch":

    score = st.session_state.main_score

    with st.container(border=True):
        st.subheader("Explore")

        if score == 4:
            st.write(TEXT_SCORE4)
            reflection = st.text_area("what do you think about it?", key="reflection_main")

        elif score == 3:
            control = st.radio(
                "Do you think you can control your actions?",
                ["Yes", "No"],
                key="control_radio",
            )

            if st.button("Continue"):
                st.session_state.control_choice = control
                if control == "Yes":
                    st.session_state.step = "sub_quiz"
                else:
                    st.session_state.step = "end"
                st.rerun()

        else:
            st.write(TEXT_CAVE_REFLECTION)
            reflection = st.text_area("what now?", key="reflection_main")

# --------------------------------------------------
# STEP 3: METACOGNITION SUB-QUIZ (only if control == "Yes")
# --------------------------------------------------

elif st.session_state.step == "sub_quiz":

    st.header("Let's try metacognition")

    with st.form("sub_form"):
        responses = []
        for i, question in enumerate(METACOGNITION_QUESTIONS):
            answer = st.radio(
                f"{i + 1}. {question}",
                ["ہاں", "نہیں"],
                key=f"sub_q_{i}",
                horizontal=True,
            )
            responses.append(answer)

        sub_submitted = st.form_submit_button("Submit 👀")

    if sub_submitted:
        st.session_state.sub_score = sum(a == "ہاں" for a in responses)
        st.session_state.step = "end"
        st.rerun()

# --------------------------------------------------
# STEP 4: END / FINAL EXPLORE BOX
# --------------------------------------------------

elif st.session_state.step == "end":

    with st.container(border=True):
        if st.session_state.sub_score is not None:
            if st.session_state.sub_score < 3:
                st.subheader("Explore 🔍")
                st.write(TEXT_LOW_SUBSCORE)
            else:
                st.subheader("Explore 🔓")
                st.write(TEXT_HIGH_SUBSCORE)
        else:
            st.subheader("Explore")
            st.write("Thanks for reflecting honestly — that's the first step.")

        reflection = st.text_area("what now?", key="reflection_end")

    st.success("You reached the end.")
    st.write(f"Total signal: {st.session_state.main_score} / {len(MAIN_QUESTIONS)}")

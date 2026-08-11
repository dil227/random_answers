import streamlit as st

st.set_page_config(
    page_title="Curiosity Box",
    layout="centered"
)

st.title("Answer 5 questions. See what opens next. 👀")


# ==================================================
# SESSION STATE
# ==================================================

defaults = {
    "stage_one_done": False,
    "stage_one_score": 0,
    "meta_done": False,
    "meta_score": 0,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==================================================
# STAGE 1 — CURIOSITY
# ==================================================

questions = [
    "When something is unknown, do you usually become curious rather than afraid? — تجسس / خوف",

    "When motivation disappears, can you still continue something you decided was important? — ثابت قدمی",

    "After spending a long time alone, do you begin to seek meaningful human connection? — تعلق / صحبت",

    "During disagreement, do you try to understand the other person before trying to prove yourself right? — فہم / انا",

    "When the future is uncertain, can you tolerate not knowing without immediately imagining the worst? — بے یقینی"
]


if not st.session_state.stage_one_done:

    st.caption("Five questions. No labels. Just answer.")

    with st.form("curiosity_form"):

        answers = []

        for i, question in enumerate(questions):

            answer = st.radio(
                question,
                ["Yes", "No"],
                key=f"curiosity_{i}",
                horizontal=True
            )

            answers.append(answer)

        submitted = st.form_submit_button("Explore")

    if submitted:

        st.session_state.stage_one_score = sum(
            answer == "Yes"
            for answer in answers
        )

        st.session_state.stage_one_done = True

        st.rerun()


# ==================================================
# EXPLORE
# ==================================================

if st.session_state.stage_one_done:

    score = st.session_state.stage_one_score

    with st.container(border=True):

        st.subheader("Explore")


        # ==================================================
        # PATH A — SCORE 4–5
        # ==================================================

        if score >= 4:

            st.write("""
### Time — وقت

**وَالْعَصْرِ**

*By time.*

**إِنَّ الْإِنسَانَ لَفِي خُسْرٍ**

*Humanity is truly in loss.*

You can be curious, intelligent, disciplined,
and still lose the one resource you cannot recover:

**time.**

So perhaps the interesting question is not:

> *What do I know?*

but:

> **What is my knowledge turning me into?**

Information without transformation may simply become
another way of spending time.
""")

            st.text_area(
                "What does this make you think about?",
                key="time_reflection"
            )


        # ==================================================
        # PATH B — SCORE 3
        # ==================================================

        elif score == 3:

            st.write("""
You seem to sit somewhere between **curiosity** and **uncertainty**.

That makes the next question more interesting:

### Control — اختیار

How much of what happens next is actually yours?
""")

            control = st.radio(
                "Do you believe you can meaningfully influence your own actions?",
                ["Yes", "No"],
                key="control",
                horizontal=True
            )


            # ==============================================
            # CONTROL = YES
            # ==============================================

            if control == "Yes":

                st.write("""
Then let's move one layer inward.

Knowing that you *can* act is different from noticing
**how you choose your action.**

That is metacognition.
""")


                # ==========================================
                # METACOGNITION QUESTIONS
                # ==========================================

                meta_questions = [

                    "When reality violates your plan, can you remain patient before reacting? — صبر",

                    "Can you separate what is actually within your control from what is not? — اختیار",

                    "When circumstances become difficult, do your principles remain stable? — ثابت قدمی",

                    "When you cannot predict what comes next, can trust coexist with uncertainty? — توکل",

                    "Before acting on a strong emotion, can you observe it first? — حکمت"
                ]


                if not st.session_state.meta_done:

                    with st.form("meta_form"):

                        meta_answers = []

                        for i, question in enumerate(meta_questions):

                            answer = st.radio(
                                question,
                                ["Yes", "No"],
                                key=f"meta_{i}",
                                horizontal=True
                            )

                            meta_answers.append(answer)

                        meta_submit = st.form_submit_button(
                            "Go deeper →"
                        )

                    if meta_submit:

                        st.session_state.meta_score = sum(
                            answer == "Yes"
                            for answer in meta_answers
                        )

                        st.session_state.meta_done = True

                        st.rerun()


                # ==========================================
                # META RESULT
                # ==========================================

                if st.session_state.meta_done:

                    meta_score = st.session_state.meta_score


                    # --------------------------------------
                    # LOWER META SCORE
                    # --------------------------------------

                    if meta_score < 4:

                        with st.container(border=True):

                            st.subheader("Explore 🔍")

                            st.write("""
### Patience — صبر

An unwanted outcome does not automatically mean
the direction was wrong.

Can you remain aligned when reality does not immediately
reward the choice?


### Reform — اصلاح

You are not responsible for controlling everything.

You are responsible for improving what falls
within your capacity.

**11:88**


### Steadfastness — ثابت قدمی

Difficulty creates pressure to abandon direction.

The Qur'an repeatedly answers that pressure
with steadfastness, prayer and patience.

**11:112–115**


### Trust — توکل

Trust is most meaningful precisely when the outcome
cannot yet be known.

**11:123**


### Wisdom — حکمت

Not every internal signal deserves an external action.

Sometimes wisdom is the distance between:

**feeling → observing → choosing**

That distance is where metacognition begins.
""")


                    # --------------------------------------
                    # HIGH META SCORE
                    # --------------------------------------

                    else:

                        with st.container(border=True):

                            st.subheader("Explore 🔓")

                            st.write("""
You seem comfortable with **agency — اختیار**.

So the harder problem may be:

### What happens when agency reaches its limit?


**Beautiful patience — صبرِ جمیل**

Some things cannot be fixed by another action.

Can acceptance exist without giving up direction?

**12:18**

Patience — صبر
Surah Yusuf presents patience not as passivity,
 but as stability under incomplete information. 
 Yaqub loses Yusuf without knowing where he is, whether he will return, or why this happened. 
 His response is ṣabrun jamīl — صبرِ جمیل, “beautiful patience” (12:18). 
 Later, after another loss, he repeats it (12:83). He grieves deeply,
  yet does not abandon hope (12:86–87).
Core idea: patience is continuing in the right direction
 when the outcome is still hidden.
### Desire — خواہش

A desire can be real without being a command.

Can you experience wanting something
without automatically obeying the wanting?

**12:23**


### Direction — راستہ

Sometimes the right action is more uncomfortable
than the wrong one.

Can meaning outweigh immediate comfort?

**12:33**


### Change — تبدیلی

The Qur'an makes an unusual move:

it connects changes in the external condition
with changes within the self.

**13:11**

Perhaps control is neither:

**"I control everything"**

nor

**"I control nothing."**

Perhaps it is:

> **Act where you have اختیار.  
> Practice توکل where you don't.**
""")


            # ==============================================
            # CONTROL = NO
            # ==============================================

            else:

                st.write("""
Interesting.

Then instead of asking whether you control **events**,
let's shrink the problem.

Maybe you cannot control what appears in consciousness.

But can you influence what happens **after** it appears?

A thought arrives.

An emotion follows.

Then there is a small gap.

### اختیار

Perhaps freedom lives inside that gap:

**stimulus → awareness → choice**

Not absolute control.

Just enough control for direction.
""")


        # ==================================================
        # PATH C — SCORE 0–2
        # ==================================================

        else:

            st.write("""
Let's explore a different problem.

### What if your perception is incomplete?

Surah Al-Kahf repeatedly places human beings
inside situations they initially misunderstand.


### The Cave — ایمان

The obvious safe choice and the meaningful choice
are not always the same.

**18:9–26**


### The Two Gardens — دنیا

Something can look permanent precisely because
we are observing it from inside a short time window.

**18:32–46**


### Musa & Khidr — علم

Musa observes events that appear irrational.

Only later does additional information change
their meaning.

**18:60–82**

The event did not change.

**The available information changed.**


### Patience — صبر

This explains Khidr's question:

> How can you be patient with something
> you do not yet comprehend?

**18:68**

Judgment came before complete information.


### Dhul-Qarnayn — طاقت

Greater power does not remove responsibility.

It increases it.

**18:83–98**


### Human knowledge — علم

And then comes perhaps the deepest epistemic constraint:

**18:109**

Human knowledge is finite.

Reality is not required to fit inside
our current model of it.


So curiosity may eventually produce a paradox:

The more you genuinely learn,

the more clearly you can see the boundary between

**what you know**

and

**what you do not know — لا علم**
""")


            st.text_area(
                "What changed in how you see the problem?",
                key="kahf_reflection"
            )


# ==================================================
# RESET
# ==================================================

if st.session_state.stage_one_done:

    st.divider()

    if st.button("Start again ↻"):

        st.session_state.clear()
        st.rerun()
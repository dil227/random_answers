import streamlit as st
import random

from streamlit import columns
#data

with st.sidebar:
    st.title("**Correcting Behaviours MAP**")
    page = st.radio("Menu?",
                    [
                        "Home",
                        "Making goals",
                        "Distress therapy",
                        "mood"
                    ])
if page== "Home":
    st.title("**Correcting Behaviours MAP**")

elif page == "mood":
    mood = ["Sad",
            "happy",
            "neutral",
            "awwful",
            "Frustrated",
            "Startled",
            "hurt",
            "Empty",
            "fragile",
            "lonely",
            "grief",
            "uncertain",
            "Disappointed"]
    st.caption("Mood and skills")
    moodSelected= st.radio("What do you feel?", mood)
    with st.container(border=True):
        if moodSelected == "Sad":
            skills = ["Supplication",
                      "Indeed ,hearts find comfort in His remembrance",]
        elif moodSelected=="uncertain":
            skills=["Tawakkul",
                    "God is the only protector"]
        elif moodSelected=="Frustrated":
            skills=["وَوَضَعْنَا عَنكَ وِزْرَكَ","Indeed he loves those "
                                                 "who put their "
                                                 "trust in Him",
                                                 "And which favor of your"
                                                 " Lord will you deny!"]

        elif moodSelected == "happy":
            skills = [ "Generosity","He is Gani"]
        elif moodSelected == "hurt":
            skills = [ "gratitude","He is Al-hakeem!",
                       "Surely! in remembrance "
                                   "of Allah do heart finds comfort"]
        elif moodSelected == "fragile":
            skills = ["Then to Allah is your return",
                      "He alone is the refugee"]
        elif moodSelected == "grief":
            skills = ["Seek guidance through sbr and salah",
                      "إِنَّ مَعَ الْعُسْرِ يُسْرًا"
                      "He is Al-Lateef"]
        elif moodSelected == "Startled":
            skills =["أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ",
            "Indeed! He is most capable of anything"]

        elif moodSelected == "lonely":
            skills= ["وَإِلَىٰ رَبِّكَ فَارْغَب",
                     "He is Everywhere"]
        else:
            skills=["He is alpha and He is omega",
                    "He knows what you know not!"]

        for i in range(len(skills)):
            st.write(skills[i])
elif page == "Making goals":
    st.caption("Cognitive Behavioural therapy")
    tab_goal, tab_values, tab_activities = st.tabs(["Goals", "Values", "Activities"])

    with tab_goal:
        with st.container(border=True):
            st.header("Step 1: Make a goal")
            st.write(" A goal can be for a day,"
                     " A week,"
                     " A month,"
                     " A year,"
                     " A decade")
            duration = ["A day",
                        "A week",
                        "A month",
                        "6 months",
                        "A year",
                        ]
            st.multiselect("what is the duration?", duration)
            goal = st.text_input("What is the goal?", key="goal")
            measure = st.text_input("How are you going to measure the progress?", key="measure")

    with tab_values:
        with st.container(border=True):
            st.header("Step 2: Identify your values")
            st.write("What do you value most?"
                     "**YOU CAN FIND OUT IN SIMPLE STEPS**")
            st.write("1. write down your daily activities for a week")
            st.write("2. Group related activities")
            st.write("3. Identify the reasons you did each activity")

            st.checkbox("Most of your values belong to  FOLLOWING  classes:")
            st.radio("select a class", ("spirtual,connection, leisure, career, personal fitness"))

    with tab_activities:

        POINTS_PER_TASK = 25
        PRAYER_BONUS = 25
        st.write("**Check everything you did today in each domain:**")
        with st.container(border=True):
            st.title("Self Actualization")
            tasks_career = [
                "Studying",
                "Code 💻",
            ]

            st.write("It is not what an aspire to become but the conciousness of nothingess "
                     "that keeps us going!")
            career = {t: st.checkbox(t, key=f"task_{t}") for t in tasks_career}

        with st.container(border=True):
            st.title("Leisure")
            tasks_Dopamine = [
                "Hot tub 🛁",
                "Swimming 🏊",
                "Ice cream 🍦",
                "Game",
                "TV 📺",
                "Read 📖",
                "Write ✍️",
                "Drive 🚗",
                "Park 🏞️",
            ]
            dopamine = {t: st.checkbox(t, key=f"task_{t}") for t in tasks_Dopamine}
        with st.container(border=True):
            tasks_faith = [
                "Praying",
                "Reading Quran",
                "Supplication",
            ]
            faith = {t: st.checkbox(t, key=f"task_{t}") for t in tasks_faith}
        with ((st.container(border=True))):
            tasks_health = [
                "Clean 🧹",
                "Cook 🍳",
                "Protein🥩",
                "Skin care💆",
                "Exercise 🏋️",

            ]
            health = {t: st.checkbox(t, key=f"task_{t}") for t in tasks_health}
        with st.container(border=True):
            tasks_connection = [
                "Family",
                "Friends 👨‍👩‍👧"
            ]
            connection = {t: st.checkbox(t, key=f"task_{t}") for t in tasks_connection}

            # --- Scores ---
        all_tasks = {**career, **dopamine, **faith, **health, **connection}
        score_daily = sum(all_tasks.values()) * POINTS_PER_TASK
        st.write("### Daily productivity score:", score_daily)

        with st.container(border=True):
            if score_daily <= 100:
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.write("** What activity involves less time and energy?** 🧘")
                with c2:
                    st.write("**you dont have to leave  your comfort zone  "
                             " Zone for this one**")
                with c3:
                    st.write("**Pair first task with music**")
            elif score_daily <= 200:
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.write("**Maybe go out?**")
                with c2:
                    st.write("**Do it for the sake of doing it?**")
                with c3:
                    st.write("**Today's efforts(Serotonin) will bring tomorrow's results**")
            elif score_daily <= 300:
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.write("**What do you think is the main driver for "
                             "high level productivity?**")
                with c2:
                    st.write("**Sometimes I wonder, if "
                             "I set expectation too high to fail**")
                with c3:
                    st.write("**Its not until you fall that "
                             "you fly!**")

            elif score_daily <= 400:
                mood = "Peace"

            st.divider()
            st.title("**for i in tasks"
                     " correlate m in mood**")
    # -----------------------
elif page == "DB therapy":
    st.title("Distress tolerance therapy")
    st.header("step one: Relax")

    thought_1 = st.text_input("What is first thought??", key="t1")
    st.text_input("what is past experience with this thought?", key="p1")
    thought_2 = st.text_input("What is second thought??")
    st.text_input("what is past experience with 2nd thought?", key="p2")
    thought_3 = st.text_input("What is 3rd thought??")
    st.text_input("what is past experience with 3rd thought?", key="p3")
    thought_4 = st.text_input("What is fourth thought??")
    st.text_input("what is past experience with 4th thought?", key="p4")

    # Display chain
    st.write(
        f"{thought_1} → {thought_2} → {thought_3} → {thought_4}")

    st.header("Step Two:Evaluate")
    st.text_input("What emotions are stronger?")

    st.header("Step 3: Select Actions")
    wanting = st.text_input("What do you want to do?")
    can_do = st.text_input("What you can do?")

    st.header("Step 4: Take Actions")

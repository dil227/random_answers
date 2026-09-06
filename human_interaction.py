import random
import streamlit as st

st.set_page_config(
    page_title="Metacognition MAP",
    page_icon="🧠",
    layout="wide",
)

# ============================================================
# GLOBAL DATA
# ============================================================

BINARY_ANS = ["yes", "No"]
POINTS_PER_TASK = 25

PAGES = [
    "🏠 Home",
    "🔁 For Loop",
    "🧊 Explore Box",
    "🤝 Human Interaction Algorithm",
    "✈️ Travel",
    "♻️ Recursive Loop",
]

STATE_PLACES = {
    'Alabama': ['Gulf Shores', 'U.S. Space & Rocket Center', 'Little River Canyon', 'Birmingham Civil Rights Institute', 'Cheaha State Park'],
    'Alaska': ['Denali National Park', 'Glacier Bay National Park', 'Kenai Fjords National Park', 'Mendenhall Glacier', 'Fairbanks'],
    'Arizona': ['Grand Canyon', 'Sedona', 'Antelope Canyon', 'Monument Valley', 'Saguaro National Park'],
    'Arkansas': ['Hot Springs National Park', 'Buffalo National River', 'Crystal Bridges Museum', 'Petit Jean State Park', 'Mount Magazine'],
    'California': ['Yosemite National Park', 'Big Sur', 'Golden Gate Bridge', 'Joshua Tree National Park', 'Lake Tahoe'],
    'Colorado': ['Rocky Mountain National Park', 'Garden of the Gods', 'Aspen', 'Telluride', 'Great Sand Dunes National Park'],
    'Connecticut': ['Mystic Seaport', 'Yale University', 'Gillette Castle', 'Hammonasset Beach', 'Mark Twain House'],
    'Delaware': ['Rehoboth Beach', 'Cape Henlopen State Park', 'Winterthur Museum', 'Bethany Beach', 'Delaware Water Gap'],
    'Florida': ['Everglades National Park', 'Key West', 'Miami Beach', 'Walt Disney World', 'St. Augustine'],
    'Georgia': ['Savannah Historic District', 'Atlanta BeltLine', 'Stone Mountain', 'Jekyll Island', 'Blue Ridge'],
    'Hawaii': ['Waikiki Beach', 'Haleakalā National Park', 'Nā Pali Coast', 'Hawaiʻi Volcanoes National Park', 'Road to Hana'],
    'Idaho': ['Shoshone Falls', 'Sawtooth Mountains', 'Craters of the Moon', "Coeur d'Alene", 'Sun Valley'],
    'Illinois': ['Millennium Park', 'Art Institute of Chicago', 'Starved Rock State Park', 'Navy Pier', 'Abraham Lincoln Presidential Library'],
    'Indiana': ['Indiana Dunes National Park', 'Indianapolis Motor Speedway', 'Turkey Run State Park', 'Monument Circle', 'Brown County State Park'],
    'Iowa': ['Field of Dreams', 'Maquoketa Caves', 'Iowa State Capitol', 'Pikes Peak State Park', 'Amana Colonies'],
    'Kansas': ['Monument Rocks', 'Tallgrass Prairie National Preserve', 'Keeper of the Plains', 'Cosmosphere', 'Botanica Wichita'],
    'Kentucky': ['Mammoth Cave National Park', 'Churchill Downs', 'Red River Gorge', 'Cumberland Falls', 'Louisville Slugger Museum'],
    'Louisiana': ['French Quarter', 'Garden District', 'Atchafalaya Basin', 'Oak Alley Plantation', 'National WWII Museum'],
    'Maine': ['Acadia National Park', 'Portland Head Light', 'Bar Harbor', 'Baxter State Park', 'Old Orchard Beach'],
    'Maryland': ['Inner Harbor', 'Assateague Island', 'Antietam National Battlefield', 'Annapolis Historic District', 'Deep Creek Lake'],
    'Massachusetts': ['Freedom Trail', 'Cape Cod', "Martha's Vineyard", 'Fenway Park', 'Salem'],
    'Michigan': ['Pictured Rocks National Lakeshore', 'Mackinac Island', 'Sleeping Bear Dunes', 'Detroit Institute of Arts', 'Tahquamenon Falls'],
    'Minnesota': ['Boundary Waters', 'Voyageurs National Park', 'Mall of America', 'North Shore Scenic Drive', 'Minnehaha Falls'],
    'Mississippi': ['Natchez Trace Parkway', 'Vicksburg National Military Park', 'Biloxi Beach', 'Elvis Presley Birthplace', 'Oxford Square'],
    'Missouri': ['Gateway Arch', 'Lake of the Ozarks', 'Silver Dollar City', 'Forest Park', 'Ha Ha Tonka State Park'],
    'Montana': ['Glacier National Park', 'Yellowstone North Entrance', 'Going-to-the-Sun Road', 'Flathead Lake', 'Big Sky'],
    'Nebraska': ['Henry Doorly Zoo', 'Scotts Bluff National Monument', 'Chimney Rock', 'Sandhills', 'Strategic Air Command Museum'],
    'Nevada': ['Las Vegas Strip', 'Red Rock Canyon', 'Lake Tahoe', 'Valley of Fire', 'Great Basin National Park'],
    'New Hampshire': ['Mount Washington', 'White Mountain National Forest', 'Franconia Notch', 'Lake Winnipesaukee', 'Kancamagus Highway'],
    'New Jersey': ['Cape May', 'Liberty State Park', 'Atlantic City Boardwalk', 'Delaware Water Gap', 'Princeton University'],
    'New Mexico': ['White Sands National Park', 'Santa Fe Plaza', 'Carlsbad Caverns', 'Taos Pueblo', 'Bandelier National Monument'],
    'New York': ['Times Square', 'Niagara Falls', 'Adirondack Mountains', 'Central Park', 'Finger Lakes'],
    'North Carolina': ['Blue Ridge Parkway', 'Great Smoky Mountains', 'Outer Banks', 'Biltmore Estate', 'Chimney Rock'],
    'North Dakota': ['Theodore Roosevelt National Park', 'Enchanted Highway', 'Fort Union Trading Post', 'Lake Sakakawea', 'Maah Daah Hey Trail'],
    'Ohio': ['Rock & Roll Hall of Fame', 'Hocking Hills State Park', 'Cedar Point', 'Cuyahoga Valley National Park', 'National Museum of the U.S. Air Force'],
    'Oklahoma': ['Wichita Mountains', 'Oklahoma City National Memorial', 'Philbrook Museum', 'Route 66', 'Turner Falls'],
    'Oregon': ['Crater Lake National Park', 'Cannon Beach', 'Columbia River Gorge', 'Mount Hood', 'Bend'],
    'Pennsylvania': ['Liberty Bell', 'Gettysburg National Military Park', 'Fallingwater', 'Pocono Mountains', 'Philadelphia Museum of Art'],
    'Rhode Island': ['Newport Cliff Walk', 'The Breakers', 'Block Island', 'Narragansett Beach', 'Providence WaterFire'],
    'South Carolina': ['Charleston Historic District', 'Myrtle Beach', 'Hilton Head Island', 'Congaree National Park', 'Hunting Island State Park'],
    'South Dakota': ['Mount Rushmore', 'Badlands National Park', 'Custer State Park', 'Crazy Horse Memorial', 'Spearfish Canyon'],
    'Tennessee': ['Great Smoky Mountains', 'Nashville Broadway', 'Graceland', 'Lookout Mountain', 'Dollywood'],
    'Texas': ['Big Bend National Park', 'San Antonio River Walk', 'Space Center Houston', 'Guadalupe Mountains', 'Austin'],
    'Utah': ['Zion National Park', 'Bryce Canyon', 'Arches National Park', 'Canyonlands', 'Capitol Reef'],
    'Vermont': ['Stowe', 'Green Mountain National Forest', 'Lake Champlain', 'Woodstock', "Smugglers' Notch"],
    'Virginia': ['Shenandoah National Park', 'Colonial Williamsburg', 'Virginia Beach', 'Mount Vernon', 'Blue Ridge Parkway'],
    'Washington': ['Mount Rainier National Park', 'Olympic National Park', 'North Cascades', 'Pike Place Market', 'San Juan Islands'],
    'West Virginia': ['New River Gorge National Park', 'Blackwater Falls', 'Seneca Rocks', 'Harpers Ferry', 'Snowshoe Mountain'],
    'Wisconsin': ['Door County', 'Apostle Islands', 'Wisconsin Dells', 'Milwaukee Art Museum', "Devil's Lake State Park"],
    'Wyoming': ['Yellowstone National Park', 'Grand Teton National Park', 'Devils Tower', 'Jackson Hole', 'Hot Springs State Park'],
}


# Standalone page: 🤝 Human Interaction Algorithm
if True:
    st.header("🤝 Human Interaction Algorithm")
    st.caption("A nested if / elif perception and response model.")

    topics_hawk = [
        "Technology/Innovation",
        "Work",
        "Politics",
        "Sports",
        "Current affairs",
    ]

    topics_dove = [
        "Experience",
        "Organizing",
        "Fashion",
    ]

    with st.container(border=True):
        connection = st.radio(
            "Does it have to be a connection?",
            BINARY_ANS,
            index=None,
            key="human_connection",
        )

        if connection == "yes":
            connection_type = st.radio(
                "What type of connection is this?",
                ["Desirable", "Undesirable"],
                index=None,
                key="connection_type",
            )

            if connection_type == "Desirable":
                appearance = st.radio(
                    "How does their appearance affect your first impression?",
                    ["Attractive", "Neutral", "Not attractive"],
                    index=None,
                    key="appearance",
                )

                if appearance == "Attractive":
                    st.write("Appearance creates attention; now test the deeper variables.")

                    smartness = st.radio(
                        "Are they smart?",
                        BINARY_ANS,
                        index=None,
                        key="smartness",
                    )

                    if smartness == "yes":
                        respect = st.radio(
                            "Are they respectful?",
                            BINARY_ANS,
                            index=None,
                            key="respect",
                        )

                        if respect == "yes":
                            care = st.radio(
                                "Are they caring?",
                                BINARY_ANS,
                                index=None,
                                key="care",
                            )

                            if care == "yes":
                                generous = st.radio(
                                    "Are they generous?",
                                    BINARY_ANS,
                                    index=None,
                                    key="generous",
                                )

                                if generous == "yes":
                                    passionate = st.radio(
                                        "Are they passionate?",
                                        BINARY_ANS,
                                        index=None,
                                        key="passionate",
                                    )

                                    if passionate == "yes":
                                        genuine = st.radio(
                                            "Are they genuine?",
                                            BINARY_ANS,
                                            index=None,
                                            key="genuine",
                                        )

                                        if genuine == "yes":
                                            st.success(
                                                "Rare combination. Continue observing reality."
                                            )

                                        elif genuine == "No":
                                            st.info(
                                                "Attraction is high, but information is incomplete."
                                            )

                                    elif passionate == "No":
                                        st.write(
                                            "The connection may be stable without being intense."
                                        )

                                elif generous == "No":
                                    st.write(
                                        "Check whether generosity is actually a core value for you."
                                    )

                            elif care == "No":
                                st.warning(
                                    "Attraction without care may not support the connection you want."
                                )

                        elif respect == "No":
                            jerk = st.radio(
                                "Are they consistently disrespectful?",
                                BINARY_ANS,
                                index=None,
                                key="jerk",
                            )

                            if jerk == "yes":
                                st.error("Reduce exposure or use clear boundaries.")
                            elif jerk == "No":
                                st.info("Gather more information before labeling the pattern.")

                    elif smartness == "No":
                        st.write(
                            "Decide whether intellectual compatibility is actually necessary."
                        )

                elif appearance == "Neutral":
                    st.write(
                        "Neutral appearance gives you room to observe behavior with less intensity."
                    )

                    curiosity = st.radio(
                        "Are you curious enough to know them better?",
                        BINARY_ANS,
                        index=None,
                        key="neutral_curiosity",
                    )

                    if curiosity == "yes":
                        st.success("Talk, observe, and update your model.")
                    elif curiosity == "No":
                        st.info("No need to force a connection.")

                elif appearance == "Not attractive":
                    desperation = st.radio(
                        "Are you trying to force interest?",
                        BINARY_ANS,
                        index=None,
                        key="desperation",
                    )

                    if desperation == "yes":
                        st.write(
                            "Ask whether loneliness or urgency is changing your standards."
                        )
                    elif desperation == "No":
                        family = st.radio(
                            "Is this family or another necessary relationship?",
                            BINARY_ANS,
                            index=None,
                            key="family",
                        )

                        if family == "yes":
                            st.info("Use relationship-specific values rather than attraction.")
                        elif family == "No":
                            st.write("You may simply choose not to pursue it.")

            elif connection_type == "Undesirable":
                encounter = st.radio(
                    "Is more than one encounter probable?",
                    BINARY_ANS,
                    index=None,
                    key="encounter",
                )

                if encounter == "yes":
                    chosen_strategy = st.radio(
                        "Choose interaction strategy",
                        ["Hawk", "Dove", "Retaliator", "Prober-Retaliator"],
                        index=None,
                        key="chosen_strategy",
                    )

                    if chosen_strategy == "Hawk":
                        st.write("Hawk: assertive and willing to escalate conflict.")
                        st.radio(
                            "Choose a topic",
                            topics_hawk,
                            index=None,
                            key="hawk_topic",
                        )

                    elif chosen_strategy == "Dove":
                        st.write("Dove: avoid unnecessary conflict and keep interaction light.")
                        st.radio(
                            "Choose a topic",
                            topics_dove,
                            index=None,
                            key="dove_topic",
                        )

                    elif chosen_strategy == "Retaliator":
                        st.write(
                            "Retaliator: begin peacefully, but respond if attacked."
                        )

                    elif chosen_strategy == "Prober-Retaliator":
                        st.write(
                            "Prober-Retaliator: cautiously test boundaries, then update."
                        )

                elif encounter == "No":
                    st.write(
                        "If the encounter is unlikely to repeat, minimize unnecessary cognitive load."
                    )

        elif connection == "No":
            probable_connection = st.radio(
                "Could it become a connection?",
                BINARY_ANS,
                index=None,
                key="probable_connection",
            )

            if probable_connection == "yes":
                st.write("Go with the flow and gather information.")
            elif probable_connection == "No":
                st.caption("Then ask why the interaction matters at all.")

    # ---------------- APPEARANCE / PERCEPTION PROFILE ----------------
    st.divider()
    st.subheader("Appearance → Attention → Interpretation → Affect → Action")

    appearance_cues = [
        "Facial expression",
        "Clothing",
        "Posture",
        "Eye contact",
        "Voice",
        "Grooming",
    ]

    st.write("What appearance cues are influencing the first impression?")
    appearance_score = {
        cue: st.checkbox(cue, key=f"appearance_cue_{cue}")
        for cue in appearance_cues
    }

    attention = [
        "Threats",
        "Opportunities",
        "Beauty",
        "Status",
        "Meaning",
        "Relationships",
    ]

    st.write("What do you notice repeatedly?")
    attention_score = {
        item: st.checkbox(item, key=f"attention_{item}")
        for item in attention
    }

    interpretation = [
        "Optimistic",
        "Pessimistic",
        "Personal Blame",
        "External Blame",
        "Logical",
        "Emotional",
        "Concrete",
        "Abstract",
    ]

    st.write("How do you explain events?")
    interpretation_score = {
        item: st.checkbox(item, key=f"interpretation_{item}")
        for item in interpretation
    }

    affect = [
        "Calm",
        "Fearful",
        "Curious",
        "Defensive",
        "Hopeful",
        "Detached",
    ]

    st.write("Dominant affect?")
    affect_score = {
        item: st.checkbox(item, key=f"affect_{item}")
        for item in affect
    }

    behavior = [
        "Avoidance",
        "Exploration",
        "Control",
        "Connection",
        "Creativity",
        "Aggression",
    ]

    st.write("What action does perception produce?")
    behavior_score = {
        item: st.checkbox(item, key=f"behavior_{item}")
        for item in behavior
    }

    perception_score = (
        sum(appearance_score.values())
        + sum(attention_score.values())
        + sum(interpretation_score.values())
        + sum(affect_score.values())
        + sum(behavior_score.values())
    )

    st.metric("Perception dimensions activated", perception_score)

    if perception_score < 5:
        st.write("Very narrow perceptual frame")
    elif perception_score < 10:
        st.write("Narrow perceptual frame")
    elif perception_score < 15:
        st.write("Moderately broad frame")
    elif perception_score < 20:
        st.write("Broad frame")
    else:
        st.write("Highly multidimensional frame")

# ============================================================
# TRAVEL
# ============================================================


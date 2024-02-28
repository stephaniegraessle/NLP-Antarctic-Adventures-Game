abstract MicroLang = {

    cat
    -- Common
        Utt ;    -- sentence, question, word...         e.g. "be quiet"

    -- Cat
        S ;      -- declarative sentence                e.g. "she lives here"
        VP ;     -- verb phrase                         e.g. "lives here"
        Comp ;   -- complement of copula                e.g. "warm"
        AP ;     -- adjectival phrase                   e.g. "warm"
        CN ;     -- common noun (without determiner)    e.g. "red house"
        NP ;     -- noun phrase (subject or object)     e.g. "the red house"
        Det ;    -- determiner phrase                   e.g. "those"
        Prep ;   -- preposition, or just case           e.g. "in", dative
        V ;      -- one-place verb                      e.g. "sleep" 
        V2 ;     -- two-place verb                      e.g. "love"
        A ;      -- one-place adjective                 e.g. "warm"
        N ;      -- common noun                         e.g. "house"
        Pron ;   -- personal pronoun                    e.g. "she"
        Adv ;    -- adverbial phrase                    e.g. "in the house"

    fun
    -- Phrase
        UttS      : S  -> Utt ;         -- he walks
        UttNP     : NP -> Utt ;         -- he

    -- Sentence
        PredVPS   : NP -> VP -> S ;             -- John walks --s shortcut even wrt MiniGrammar

    -- Verb
        UseV      : V   -> VP ;             -- sleep
        ComplV2   : V2  -> NP -> VP ;       -- love it ---s
        UseComp   : Comp  -> VP ;           -- be small
        CompAP    : AP  -> Comp ;           -- small
        AdvVP     : VP -> Adv -> VP ;       -- sleep here

    -- Noun
        DetCN     : Det -> CN -> NP ;       -- the man
        UsePron   : Pron -> NP ;            -- she
        a_Det     : Det ;                   -- indefinite singular ---s
        aPl_Det   : Det ;                   -- indefinite plural   ---s
        the_Det   : Det ;                   -- definite singular   ---s
        thePl_Det : Det ;                   -- definite plural     ---s
        UseN      : N -> CN ;               -- house
        AdjCN     : AP -> CN -> CN ;        -- big house

    -- Adjective
        PositA    : A  -> AP ;              -- warm

    -- Adverb
        PrepNP    : Prep -> NP -> Adv ;     -- in the house

    -- Structural
        in_Prep   : Prep ;
        on_Prep   : Prep ;
        with_Prep : Prep ;

        he_Pron   : Pron ;
        she_Pron  : Pron ;
        they_Pron : Pron ;
        it_Pron   : Pron ;
        you_Pron  : Pron ;
        that_Pron : Pron ;

    fun
        already_Adv : Adv ;
        animal_N : N ;
        ant_N : N ;
        --antarctica_PN : PN ;
        apple_N : N ;
        baby_N : N ;
        bad_A : A ;
        beer_N : N ;
        big_A : A ;
        bike_N : N ;
        bird_N : N ;
        black_A : A ;
        blood_N : N ;
        blue_A : A ;
        bluewhale_N : N ;
        boat_N : N ;
        book_N : N ;
        boy_N : N ;
        bread_N : N ;
        break_V2 : V2 ;
        building_N : N ;
        buy_V2 : V2 ;
        car_N : N ;
        cat_N : N ;
        child_N : N ;
        city_N : N ;
        clean_A : A ;
        clever_A : A ;
        cloud_N : N ;
        cold_A : A ;
        consume_V : V ;
        consume_V2 : V2 ;
        come_V : V ;
        computer_N : N ;
        cow_N : N ;
        delicious_A : A ;
        die_V : V ;
        dirty_A : A ;
        dog_N : N ;
        drink_V2 : V2 ;
        eat_V2 : V2 ;
        egg_N : N ;
        elephantseal_N : N ;
        emperorpenguin_N : N ;
        fat_A : A ;
        find_V2 : V2 ;
        fire_N : N ;
        fish_N : N ;
        flower_N : N ;
        friend_N : N ;
        full_A : A ;
        girl_N : N ;
        glacier_N : N ;
        good_A : A ;
        go_V : V ;
        grammar_N : N ;
        green_A : A ;
        heavy_A : A ;
        horse_N : N ;
        hot_A : A ;
        house_N : N ;
        human_N : N ;
        hungry_A : A ;
        iceberg_N : N ;
        input_N : N ;
        invalid_A : A ;
        jump_V : V ;
        kill_V2 : V2 ;
        kingpenguin_N : N ;
        --know_VS : VS ;
        lake_N : N ;
        language_N : N ;
        leopardseal_N : N ;
        live_V : V ;
        love_V2 : V2 ;
        man_N : N ;
        milk_N : N ;
        mountain_N : N ;
        music_N : N ;
        new_A : A ;
        now_Adv : Adv ;
        ocean_N : N ;
        old_A : A ;
        orca_N : N ;
        penguin_N : N ;
        play_V : V ;
        read_V2 : V2 ;
        ready_A : A ;
        red_A : A ;
        river_N : N ;
        run_V : V ;
        scientist_N : N ;
        sea_N : N ;
        seal_N : N ;
        see_V2 : V2 ;
        ship_N : N ;
        sleep_V : V ;
        small_A : A ;
        snow_N : N ;
        star_N : N ;
        swim_V : V ;
        teach_V2 : V2 ;
        tooth_N : N ;
        train_N : N ;
        travel_V : V ;
        tree_N : N ;
        understand_V2 : V2 ;
        wait_V2 : V2 ;
        walk_V : V ;
        warm_A : A ;
        water_N : N ;
        whale_N : N ;
        white_A : A ;
        wine_N : N ;
        woman_N : N ;
        yellow_A : A ;
        young_A : A ;
}
abstract Adventure = {
    cat
        S ;                 -- sentence
        A ;                 -- adjective
        Anim ;              -- animal
        Det ;               -- determiner e.g., "the"
        Dir ;               -- cardinal direction
        Feat ;              -- feature which contains interactions
        Loc ;               -- location (permanent) e.g., "lake"
        Q ;                 -- question word, e.g., "where"
        Scen ;              -- scenery (that changes) e.g., "sunset", "cloud"
        V ;                 -- one-place verb
        V2 ;                -- two-place verb


    fun
        -- navigation
        AtLoc : Loc -> Det -> S ; -- "you are at a lake"
        GoToLoc : V -> Loc -> S ; -- "[go/walk/travel/slide/swim/waddle, etc.] to [Loc]"
        WhatHaveInq : Q -> V2 -> S ; -- "what do I have"
        WhatInInv : Q -> Feat -> S ; -- "what is in my inventory"
        WhereInq : Q -> A ; -- "where am I"

        -- commands
        VComm : V -> S ;                        -- command e.g., "sleep"
        V2DirComm : V2 -> Dir -> S ;            -- command e.g., "go north"
        V2FeatComm : V2 -> Feat -> S ;          -- command e.g., "eat fish"
        v2DetComm : V2 -> Det -> Feat -> S ;    -- command e.g., "eat a fish"

        a_Det : Det ;
        baby_A : A ;                -- e.g., "baby penguin"
        bad_A : A ;
        big_A : A ;
        bird_Anim : Anim ;
        black_A : A ;
        blue_A : A ;
        bluewhale_Anim : Anim ;
        boat_Feat : Feat ;
        break_V2 : V2 ;
        building_Feat : Feat ;
        clean_A : A ;
        clever_A : A ;
        cloud_Scen : Scen ;
        cold_A : A ;
        consume_V : V ;
        consume_V2 : V2 ;
        come_V : V ;
        delicious_A : A ;
        die_V : V ;
        dirty_A : A ;
        drink_V : V ;
        drink_V2 : V2 ;
        eat_V : V ;
        eat_V2 : V2 ;
        egg_Feat : Feat ;
        elephantseal_Anim : Anim ;
        emperorpenguin_Anim : Anim ;
        fat_A : A ;
        find_V2 : V2 ;
        fire_Feat : Feat ;
        female_A : A ;
        fish_Feat : Feat ;
        friend_Anim : Anim ;
        full_A : A ;
        glacier_Loc : Loc ;
        good_A : A ;
        go_V : V ;
        green_A : A ;
        have_V2 : V2 ;
        have_V2 : V2 ;
        health_Feat : Feat ;
        heavy_A : A ;
        hot_A : A ;
        how_Q : Q ;
        human_Anim : Anim ;
        hungry_A : A ;
        iceberg_Loc : Loc ;
        inventory_Feat : Feat ;
        laboratory_Loc : Loc ;
        lake_Loc : Loc ;
        leopardseal_Anim : Anim ;
        live_V : V ;
        love_V2 : V2 ;
        male_A : A ;
        meet_V2 : V2 ;
        mountain_Loc : Loc ;
        new_A : A ;
        ocean_Loc : Loc ;               -- synonym for "sea"
        old_A : A ;
        orange_A : A ;
        orca_Anim : Anim ;
        penguin_Anim : Anim ;
        pickup_V2 : V ;                 -- "pick up"
        play_V : V ;
        ready_A : A ;
        red_A : A ;
        river_Loc : Loc ;
        run_V : V ;
        scientist_Anim : Anim ;
        sea_Loc : Loc ;                 -- synonym for "ocean"
        seal_Anim : Anim ;
        see_V2 : V2 ;
        ship_Feat : Feat ;
        ship_Scen : Scen ;
        sleep_V : V ;
        slide_V : V ;
        slip_V : V ;
        small_A : A ;
        snow_Feat : Feat ;
        snow_Scen : Scen ;
        stars_Scen : Scen ;
        sunset_Scen : Scen ;
        swim_V : V ;
        talk_V : V ;
        that_Det : Det ;
        the_Det : Det ;
        this_Det : Det ;
        travel_V : V ;
        understand_V2 : V2;
        waddle_V : V ;
        wait_V : V ;
        walk_V : V ;
        warm_A : A ;
        water_Feat : Feat ;
        whale_Anim : Anim ;
        what_Q : Q ;
        when_Q : Q ;
        where_Q : Q ;
        white_A : A ;
        who_Q : Q ;
        yellow_A : A ;
        young_A : A ;
}
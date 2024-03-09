abstract Adventure = {
    cat
        S ;                 -- sentence
        A ;                 -- adjective
        Anim ;              -- animal
        Det ;               -- determiner e.g., "the"
        Dir ;               -- cardinal direction
        Feat ;              -- feature which contains interactions
        Loc ;               -- location (permanent) e.g., "lake"
        Prep ;              -- preposition
		Pron ;				-- pronoun
        Q ;                 -- question word, e.g., "where"
        Scen ;              -- scenery (that changes) e.g., "sunset", "cloud"
        Stat ;              -- stat e.g., hunger, HP
        V ;                 -- one-place verb
        V2 ;                -- two-place verb

    fun
        -- navigation
        QInq : Q -> S; -- "where am I"
        AtLoc : Loc -> Det -> S ; -- "you are at a lake"
        TravToLoc : V -> Loc -> S ; -- "[go/walk/travel/slide/swim/waddle, etc.] to [Loc]"
        VDirComm : V -> Dir -> S ; -- command e.g., "go north"
        V2DirComm : V2 -> Dir -> S ; -- command e.g., "go north"
        
        -- inventory/ground item management
        AddFeatPrepFeat : Det -> Feat -> Prep -> Feat -> S ;
        RemFeatPrepFeat : Det -> Feat -> Prep -> Feat -> S ;
        WhatHaveInq : Q -> V -> S ; -- "what do I have"
        WhatInDetInv : Q -> Det -> Feat -> S ; -- "what is in my inventory"
        
        -- general commands
        VComm : V -> S ; -- command e.g., "sleep"
		VDetComm : V -> Det -> S ; -- command e.g., "pick up all"/"pick up that"
        V2DetComm : V2 -> Det -> Feat -> S ; -- command e.g., "eat a fish"
		
		-- static statements
		ArentAny : S ;
		Death : S ;
        DontHave : S ;
        Invalid : S ;
		Welcome : S ;

        -- missing words
        missingdet_Det : Det ;

        -- words
        a_Det : Det ;
        acouple_Det : Det ;
		afew_Det : Det ;
        all_Det : Det ;
        an_Det : Det ;
        a_n_Det : Det ;
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
        carry_V2 : V2 ;
		catch_V2 : V2 ;
        clean_A : A ;
        clever_A : A ;
        clouds_Scen : Scen ;
        cold_A : A ;
        consume_V : V ;
        consume_V2 : V2 ;
        come_V : V ;
        delicious_A : A ;
        die_V : V ;
        dirty_A : A ;
        drink_V : V ;
        drink_V2 : V2 ;
        drop_V2 : V2 ;
        e_Dir : Dir ;
        east_Dir : Dir ;
        eat_V : V ;
        eat_V2 : V2 ;
        egg_Feat : Feat ;
        eight_Det : Det ;
        elephantseal_Anim : Anim ;
        emperorpenguin_Anim : Anim ;
        every_Det : Det ;
        fat_A : A ;
        find_V2 : V2 ;
        fire_Feat : Feat ;
        female_A : A ;
        fish_Feat : Feat ;
        fish_V : V ;
        five_Det : Det ;
        friend_Anim : Anim ;
        friendly_A : A ;
        from_Prep : Prep ;
        four_Det : Det ;
        full_A : A ;
        gain_V2 : V2 ;
        glacier_Loc : Loc ;
        get_V2 : V2 ;
        good_A : A ;
        go_V : V ;
        go_V2 : V2 ;
        grab_V2 : V2 ;
        green_A : A ;
        have_V : V ;
        have_V2 : V2 ;
        health_Feat : Feat ;
        heavy_A : A ;
        help_V : V ;
        help_V2 : V2 ;
        hot_A : A ;
        howmuch_Q : Q ;
        hp_Stat : Stat ;
        human_Anim : Anim ;
        hunger_Stat : Stat ;
        hungry_A : A ;
        ice_Feat : Feat ;
        iceberg_Loc : Loc ;
        inventory_Feat : Feat ;
        laboratory_Loc : Loc ;
        lake_Loc : Loc ;
        leopardseal_Anim : Anim ;
        lift_V2 : V2 ;
        live_V : V ;
        love_V2 : V2 ;
        male_A : A ;
        meet_V2 : V2 ;
        mountain_Loc : Loc ;
        move_V : V ;
        move_V2 : V2 ;
        my_Det : Det ;
        n_Dir : Dir ;
        new_A : A ;
        nine_Det : Det ;
        no_Det : Det ;
        north_Dir : Dir ;
        ocean_Loc : Loc ; -- synonym for "sea"
        old_A : A ;
        one_Det : Det ;
        orange_A : A ;
        orca_Anim : Anim ;
        penguin_Anim : Anim ;
        pickup_V2 : V2 ; -- "pick up"
        play_V : V ;
        punch_V2 : V2 ;
        putdown_V2 : V2 ;
        ready_A : A ;
        red_A : A ;
        river_Loc : Loc ;
        rock_Feat : Feat ;
        run_V : V ;
        s_Dir : Dir ;
        scientist_Anim : Anim ;
        sea_Loc : Loc ; -- synonym for "ocean"
        seal_Anim : Anim ;
        see_V2 : V2 ;
        setdown_V2 : V2 ;
        seven_Det : Det ;
        ship_Feat : Feat ;
        ship_Scen : Scen ;
        six_Det : Det ;
        sleep_V : V ;
        slide_V : V ;
        slip_V : V ;
        small_A : A ;
        snow_Feat : Feat ;
        snow_Scen : Scen ;
        snowfield_Loc : Loc ;
		some_Det : Det ;
        south_Dir : Dir ;
        stars_Scen : Scen ;
        sunset_Scen : Scen ;
        swim_V : V ;
        talk_V : V ;
        ten_Det : Det ;
        that_Det : Det ;
        the_Det : Det ;
        these_Det : Det ;
        this_Det : Det ;
        those_Det : Det ;
        three_Det : Det ;
        to_Prep : Prep ;
        travel_V : V ;
        two_Det : Det ;
        understand_V2 : V2 ;
        w_Dir : Dir ;
        waddle_V : V ;
        wait_V : V ;
        walk_V : V ;
        warm_A : A ;
        water_Feat : Feat ;
        west_Dir : Dir ;
        whale_Anim : Anim ;
        what_Q : Q ;
        when_Q : Q ;
        where_Q : Q ;
        white_A : A ;
        who_Q : Q ;
        yellow_A : A ;
        young_A : A ;
        zero_Det : Det ;

        zero_num_Det : Det ;
        one_num_Det : Det ;
        two_num_Det : Det ;
        three_num_Det : Det ;
        four_num_Det : Det ;
        five_num_Det : Det ;
        six_num_Det : Det ;
        seven_num_Det : Det ;
        eight_num_Det : Det ;
        nine_num_Det : Det ;
        ten_num_Det : Det ;
}
concrete AdventureEng of Adventure = {
    lincat
        S = {s : Str} ;
        A = {s : Str} ;
        Anim = {s : Str} ;
        Det = {s : Str} ;
        Dir = {s : Str} ;
        Feat = {s : Str} ;
        Loc = {s : Str} ;
        Prep = {s : Str} ;
		Pron = {s : Str } ;
        Q = {s : Str} ;
        Scen = {s : Str} ;
        V = {s : Str} ;
        V2 = {s : Str} ;
        
    lin
        -- navigation
        QInq q = {s = q.s ++ "am i"} ; -- "where am I", "who am I"
        ArePrepLoc pron prep det loc = {s = pron.s ++ "are" ++ prep.s ++ det.s ++ loc.s} ; -- "you are at a lake"
        PronDontV2AnyFeat pron v2 feat = {s = pron.s ++ "don't" ++ v2.s ++ "any" ++ feat.s}; -- "you don't have any fish"
        PronV2PrepLoc pron v2 prep loc = {s = pron.s ++ v2.s ++ prep.s ++ loc.s} ; -- "you move to location..."
        TravToLoc v loc = {s = v.s ++ "to" ++ loc.s} ; -- "[go/walk/travel/slide/swim/waddle, etc.] to [Loc]"
        VDirComm v dir = {s = v.s ++ dir.s} ; -- command e.g., "go north"
        V2DirComm v2 dir = {s = v2.s ++ dir.s} ; -- command e.g., "go north"
 
        -- inventory management
        AddFeatPrepFeat d f_a prep f_b = {s = "added" ++ d.s ++ f_a.s ++ prep.s ++ f_b.s} ;
        RemFeatPrepFeat d f_a prep f_b = {s = "removed" ++ d.s ++ f_a.s ++ prep.s ++ f_b.s} ;
        FeatAlone f = {s = f.s} ;
        SeeNothing = {s = "you don't see anything on the ground"} ;
        WhatHaveInq q v = {s = q.s ++ "do I" ++ v.s} ; -- "what do I have"
        WhatInDetInv q det feat = {s = q.s ++ "is in" ++ det.s ++ feat.s} ; -- "what is in my inventory"
        YourFeatIsA feat a = {s = "your" ++ feat.s ++ "is" ++ a.s} ; -- "your inventory is empty"

        -- general commands
        VComm v = {s = v.s} ; -- command e.g., "sleep"
		VDetComm v det = {s = v.s ++ det.s} ; -- command e.g., "pick up all"/"pick up that"
        V2DetComm v2 det feat = {s = v2.s ++ det.s ++ feat.s} ; -- command e.g., "eat a fish", "eat fish" (missing determiner)
		
        -- description
        PronV2DetFeat p v2 det feat = {s = p.s ++ v2.s ++ det.s ++ feat.s} ; -- "you see a fish" 

		-- static statements
		ArentAny = {s = "there aren't any"} ;
		Death = {s = "you are dead" } ;
        Goodbye = {s = "thanks for playing"} ;
        Invalid = {s = "invalid input"} ;
		Welcome = {s = "welcome to Antarctic Adventures" } ;

        missingdet_Det = {s = ""} ; -- determiner ommitted from sentence

        a_Det = {s = "a"} ;
        acouple_Det = {s = "a couple"} ;
		afew_Det = {s = "a few"} ;
        all_Det = {s = "all"} ;
        an_Det = {s = "an"} ;
        a_n_Det = {s = "a(n)"} ;
        at_Prep = {s = "at"} ;
        baby_A = {s = "baby"} ; -- e.g., "baby penguin"
        bad_A = {s = "bad"} ;
        big_A = {s = "big"};
        bird_Anim = {s = "big"} ;
        black_A = {s = "black"} ;
        blue_A = {s = "blue"} ;
        bluewhale_Anim = {s = "blue whale"} ;
        boat_Feat = {s = "boat"} ;
        break_V2 = {s = "break"};
        building_Feat = {s = "building"} ;
        carry_V2 = {s = "carry"} ;
		catch_V2 = {s = "catch"} ;
        clean_A = {s = "clean"} ;
        clever_A = {s = "clever"} ;
        clouds_Scen = {s = "clouds"} ;
        cold_A = {s = "cold"} ;
        consume_V = {s = "consume"} ;
        consume_V2 = {s = "consume"} ;
        come_V = {s = "come"} ;
        delicious_A = {s = "delicious"} ;
        die_V = {s = "die"} ;
        dirty_A = {s = "dirty"} ;
        drink_V = {s = "drink"} ;
        drink_V2 = {s = "drink"} ;
        drop_V2 = {s = "drop"} ;
        e_Dir = {s = "e"} ;
        east_Dir = {s = "east"} ;
        eat_V = {s = "eat"} ;
        eat_V2 = {s = "eat"} ;
        egg_Feat = {s = "egg"} ;
        eight_Det = {s = "eight"} ;
        elephantseal_Anim = {s = "elephant seal"} ;
        emperorpenguin_Anim = {s = "emperor penguin"} ;
        empty_A = {s = "empty"} ;
        environment_Feat = {s = "environment"} ;
        exit_V = {s = "exit"} ;
        exit_V2 = {s = "exit"} ;
        every_Det = {s = "every"} ;
        fat_A = {s = "fat"} ;
        find_V2 = {s = "find"} ;
        fire_Feat = {s = "fire"} ;
        female_A = {s = "female"} ;
        fish_Feat = {s = "fish"} ;
        fish_V = {s = "fish"} ;
        five_Det = {s = "five"} ;
        friend_Anim = {s = "friend"} ;
        friendly_A = {s = "friendly"} ;
        four_Det = {s = "four"} ;
        from_Prep = {s = "from"} ;
        full_A = {s = "full"} ;
        gain_V2 = {s = "gain"} ;
        gather_V2 = {s = "gather"} ;
        glacier_Loc = {s = "glacier"} ;
        get_V2 = {s = "get"} ;
        good_A = {s = "good"} ;
        go_V = {s = "go"} ;
        go_V2 = {s = "go"} ;
        grab_V2 = {s = "grab"} ;
        green_A = {s = "green"} ;
        have_V = {s = "have"} ;
        have_V2 = {s = "have"} ;
        health_Feat = {s = "health"} ;
        heavy_A = {s = "heavy"} ;
        help_V = {s = "help"} ;
        help_V2 = {s = "help"} ;
        hot_A = {s = "hot"} ;
        howmuch_Q = {s = "how much"} ;
        hp_Feat = {s = "hp"} ;
        human_Anim = {s = "human"} ;
        hunger_Feat = {s = "hunger"} ;
        hungry_A = {s = "hungry"} ;
        ice_Feat = {s = "ice"} ;
        iceberg_Loc = {s = "iceberg"} ;
        inventory_Feat = {s = "inventory"} ;
        laboratory_Loc = {s = "laboratory"} ;
        lake_Loc = {s = "lake"} ;
        leopardseal_Anim = {s = "leopard seal"} ;
        lift_V2 = {s = "lift"} ;
        live_V = {s = "live"} ;
        location_Feat = {s = "location"} ;
        location_Loc = {s = "location"} ;
        love_V2 = {s = "love"} ;
        male_A = {s = "male"} ;
        meet_V2 = {s = "meet"} ;
        more_Det = {s = "more"} ;
        mountain_Loc = {s = "mountain"} ;
        move_V = {s = "move"} ;
        move_V2 = {s = "move"} ;
        my_Det = {s = "my"} ;
        n_Dir = {s = "n"} ;
        new_A = {s = "new"} ;
        no_Det = {s = "no"} ;
        nine_Det = {s = "nine"} ;
        north_Dir = {s = "north"} ;
        ocean_Loc = {s = "ocean"} ; -- synonym for "sea"
        old_A = {s = "old"} ;
        one_Det = {s = "one"} ;
        orange_A = {s = "orange"} ;
        orca_Anim = {s = "orca"} ;
        penguin_Anim = {s = "penguin"} ;
        pickup_V2 = {s = "pick up"} ;             -- "pick up"
        play_V = {s = "play"} ;
        punch_V2 = {s = "punch"} ;
        putdown_V2 = {s = "put down"} ;
        quit_V = {s = "quit"} ;
        quit_V2 = {s = "quit"} ;
        ready_A = {s = "ready"} ;
        red_A = {s = "red"} ;
        river_Loc = {s = "river"} ;
        rock_Feat = {s = "rock"} ;
        run_V = {s = "run"} ;
        s_Dir = {s = "s"} ;
        scientist_Anim = {s = "scientist"} ;
        sea_Loc = {s = "sea"} ;                   -- synonym for "ocean"
        seal_Anim = {s = "seal"} ;
        see_V2 = {s = "see"} ;
        setdown_V2 = {s = "set down"} ;
        seven_Det = {s = "seven"} ;
        ship_Feat = {s = "ship"} ;
        ship_Scen = {s = "ship"} ;
        six_Det = {s = "six"} ;
        sleep_V = {s = "sleep"} ;
        slide_V = {s = "slide"} ;
        slip_V = {s = "slip"} ;
        small_A = {s = "small"} ;
        snow_Feat = {s = "snow"} ;
        snow_Scen = {s = "snow"} ;
        snowfield_Loc = {s = "snow field"} ;
		some_Det = {s = "some"} ;
        south_Dir = {s = "south"} ;
        stars_Scen = {s = "stars"} ;
        sunset_Scen = {s = "sunset"} ;
        swim_V = {s = "swim"} ;
        take_V2 = {s = "take"} ;
        talk_V = {s = "talk"} ;
        ten_Det = {s = "ten"} ;
        that_Det = {s = "that"} ;
        the_Det = {s = "the"} ;
        these_Det = {s = "these"} ;
        this_Det = {s = "this"} ;
        those_Det = {s = "those"} ;
        three_Det = {s = "three"} ;
        to_Prep = {s = "to"} ;
        travel_V = {s = "travel"} ;
        two_Det = {s = "two"} ;
        understand_V2 = {s = "understand"};
        w_Dir = {s = "w"} ;
        waddle_V = {s = "waddle"} ;
        wait_V = {s = "wait"} ;
        walk_V = {s = "walk"} ;
        warm_A = {s = "warm"} ;
        water_Feat = {s = "water"} ;
        west_Dir = {s = "west"} ;
        whale_Anim = {s = "whale"} ;
        what_Q = {s = "what"} ;
        when_Q = {s = "when"} ;
        where_Q = {s = "where"} ;
        white_A = {s = "white"} ;
        who_Q = {s = "who"} ;
        yellow_A = {s = "yellow"} ;
        you_Pron = {s = "you"} ;
        young_A = {s = "young"} ;
        zero_Det = {s = "zero"} ;

        zero_num_Det = {s = "0"} ;
        one_num_Det = {s = "1"} ;
        two_num_Det = {s = "2"} ;
        three_num_Det = {s = "3"} ;
        four_num_Det = {s = "4"} ;
        five_num_Det = {s = "5"} ;
        six_num_Det = {s = "6"} ;
        seven_num_Det = {s = "7"} ;
        eight_num_Det = {s = "8"} ;
        nine_num_Det = {s = "9"} ;
        ten_num_Det = {s = "10"} ;
}
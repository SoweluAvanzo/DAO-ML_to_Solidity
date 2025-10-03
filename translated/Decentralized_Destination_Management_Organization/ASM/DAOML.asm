asm DAOML



import ../lib/StandardLibrary





signature : 

    abstract domain User

    abstract domain Permission

    abstract domain Entity

    abstract domain GovernanceArea

    enum domain EntityType = {ROLE, COMMITTEE}

    enum domain Operation = {ASSIGNROLE, REVOKEROLE, GRANTPERM, REVOKEPERM }



	

    controlled controls : Prod(Entity, Entity) -> Boolean

    

    controlled associate : Prod(Entity, Permission) -> Boolean



    controlled aggregationRole : Entity -> Entity

    controlled aggregationCommittee : Entity -> Entity



    controlled into : Permission -> GovernanceArea



    controlled roles : User -> Entity



    controlled type : Entity -> EntityType



    // Roles

    

    static ddmo_member : Entity

    

    static magister : Entity

    

    static host : Entity

    

    static analyst : Entity

    

    static worker : Entity

    

    static student : Entity

    

    static ddmo_board_member : Entity

    

    static freelancer : Entity

    

    static institutional_representative : Entity

    

    static mentor : Entity

    

    static decentralized_destination_management_organizationowner : Entity

    

    static owner_role : Entity // for owner - controls all the roles - has all the permissions



    // Committees

    

    static ddmo_council : Entity

    

    // Permissions

    

    static supply_service : Entity

    

    static propose_task_delegation : Entity

    

    static execute_task : Entity

    

    static share_task : Entity

    

    static report_task_unaccomplishment : Entity

    

    static block_user : Entity

    

    static trigger_dispute_resolution : Entity

    

    static oversee_dispute : Entity

    

    static approve_kyb : Entity

    

    static resolve_dispute : Entity

    

    static suspend_ddmo : Entity

    

    static liquidate_ddmo : Entity

    

    static merge_ddmo : Entity

    

    static access_data : Entity

    

    static update_destination_portal : Entity

    

    static approve_ai_recommendations : Entity

    

    static update_duration_of_user_block : Entity

    

    static update_number_of_council_participants : Entity

    

    static request_ddmo_change : Entity

    

    static ddmo_council_voting_right : Entity

    

    static ddmo_council_proposal_right : Entity

       



    // Governance Areas

    

    // Users

    

    static owner : User

    derived controlledBy : Prod(Entity, Entity) -> Boolean

    derived hasPermission : Prod(Entity, Permission) -> Boolean



    // Monitored functions (sender actions)

    monitored sender : User

    monitored mUser : User

    monitored mEntity : Entity

    monitored mPermission : Permission

    monitored mOperation : Operation



definitions : 



    function controlledBy ($e in Entity, $sender in Entity) =

        if controls($sender, $e) then

            true

        else

        	if isDef(aggregationRole($sender)) then

                controlledBy(aggregationRole($sender), $e)

            else 

            	if isDef(aggregationCommittee($sender)) then

            		controlledBy(aggregationCommittee($sender), $e)

            	else

                	false

                endif

            endif

        endif

        



    function hasPermission ($e in Entity, $p in Permission) = 

        if associate($e, $p) then

            true

        else

            if isDef(aggregationRole($e)) then

                hasPermission(aggregationRole($e), $p)

            else

                if isDef(aggregationCommittee($e)) then

            		hasPermission(aggregationCommittee($e), $p)

            	else

                	false

                endif

            endif

        endif





    rule r_assignRole ($u in User, $e in Entity) = 

	    if isDef(roles($u)) then

	        if controlledBy(roles($u), roles(sender)) and controlledBy($e, roles(sender)) then 

	            roles($u) := $e

	        endif

	    else

	    	if controlledBy($e, roles(sender)) then

	    		roles($u) := $e

	    	endif

	    endif



    rule r_revokeRole ($u in User, $e in Entity) = 

	    if isDef(roles($u)) then

	        if controlledBy(roles($u), roles(sender)) and controlledBy($e, roles(sender)) then 

	            roles($u) := undef

	        endif

	    endif



    rule r_grantPermission ($e in Entity, $p in Permission) = 

        if hasPermission(roles(sender), $p) and controlledBy(roles(sender), $e) then 

            associate($e, $p) := true

        endif



    rule r_revokePermission ($e in Entity, $p in Permission) = 

        if hasPermission(roles(sender), $p) and controlledBy(roles(sender), $e) then 

            associate($e, $p) := false

        endif





    invariant over hasPermission : (not hasPermission(institutional_representative, update_duration_user_block)) and (not hasPermission(institutional_representative, update_number_council_partecipants))





    main rule r_Main = 

        if isDef(roles(sender)) then

            switch mOperation

                case ASSIGNROLE : r_assignRole[mUser, mEntity]

                case REVOKEROLE : r_revokeRole[mUser, mEntity]

                case GRANTPERM : r_grantPermission[mEntity, mPermission]

                case REVOKEPERM : r_revokePermission[mEntity, mPermission]

                

                    

                

            endswitch

        endif



        





default init s0:



    function controls ($owner in Entity, $control in Entity) = 

        switch $owner

            

            case ddmo_council :

                false

            



            case owner_role : 

                switch $control

                    

                    case ddmo_member : true

                    

                    case magister : true

                    

                    case host : true

                    

                    case analyst : true

                    

                    case worker : true

                    

                    case student : true

                    

                    case ddmo_board_member : true

                    

                    case freelancer : true

                    

                    case institutional_representative : true

                    

                    case mentor : true

                    

                    case decentralized_destination_management_organizationowner : true

                    

                    

                    case ddmo_council : true

                    

                    otherwise false

                endswitch



            

            case ddmo_member :

                false

            

            case magister :

                false

            

            case host :

                false

            

            case analyst :

                false

            

            case worker :

                false

            

            case student :

                false

            

            case ddmo_board_member :

                false

            

            case freelancer :

                false

            

            case institutional_representative :

                false

            

            case mentor :

                false

            

            case decentralized_destination_management_organizationowner :

                false

            

            otherwise false

        endswitch



    function associate($e in Entity, $p in Permission) = 

        switch $e

            

                

            case ddmo_member :

                switch $p

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case magister :

                switch $p

                    

                    case block_user : true

                    

                    case oversee_dispute : true

                    

                    case trigger_dispute_resolution : true

                    

                    case resolve_dispute : true

                    

                    case ddmo_council_voting_right : true

                    

                    case ddmo_council_proposal_right : true

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case host :

                switch $p

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case analyst :

                switch $p

                    

                    case access_data : true

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case worker :

                switch $p

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case student :

                switch $p

                    

                    case access_data : true

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case ddmo_board_member :

                switch $p

                    

                    case ddmo_council_voting_right : true

                    

                    case ddmo_council_proposal_right : true

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case freelancer :

                switch $p

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case institutional_representative :

                switch $p

                    

                    case access_data : true

                    

                    case ddmo_council_voting_right : true

                    

                    case ddmo_council_proposal_right : true

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case mentor :

                switch $p

                    

                    case approve_ai_recommendations : true

                    

                    case approve_kyb : true

                    

                    case ddmo_council_voting_right : true

                    

                    case ddmo_council_proposal_right : true

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case request_ddmo_change : true

                    

                    case report_task_unaccomplishment : true

                    

                    otherwise false

                endswitch

                

            

                

            case decentralized_destination_management_organizationowner :

                switch $p

                    

                    case supply_service : true

                    

                    case propose_task_delegation : true

                    

                    case execute_task : true

                    

                    case share_task : true

                    

                    case report_task_unaccomplishment : true

                    

                    case block_user : true

                    

                    case trigger_dispute_resolution : true

                    

                    case oversee_dispute : true

                    

                    case approve_kyb : true

                    

                    case resolve_dispute : true

                    

                    case suspend_ddmo : true

                    

                    case liquidate_ddmo : true

                    

                    case merge_ddmo : true

                    

                    case access_data : true

                    

                    case update_destination_portal : true

                    

                    case approve_ai_recommendations : true

                    

                    case update_duration_of_user_block : true

                    

                    case update_number_of_council_participants : true

                    

                    case request_ddmo_change : true

                    

                    case ddmo_council_voting_right : true

                    

                    case ddmo_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

            

            

                

            case ddmo_council :

                switch $p

                    

                    case update_duration_of_user_block : true

                    

                    case suspend_ddmo : true

                    

                    case liquidate_ddmo : true

                    

                    case merge_ddmo : true

                    

                    case update_destination_portal : true

                    

                    case update_number_of_council_participants : true

                    

                    otherwise false

                endswitch

                

            



            case owner_role : 

                switch $p

                

                    case supply_service : true

                

                    case propose_task_delegation : true

                

                    case execute_task : true

                

                    case share_task : true

                

                    case report_task_unaccomplishment : true

                

                    case block_user : true

                

                    case trigger_dispute_resolution : true

                

                    case oversee_dispute : true

                

                    case approve_kyb : true

                

                    case resolve_dispute : true

                

                    case suspend_ddmo : true

                

                    case liquidate_ddmo : true

                

                    case merge_ddmo : true

                

                    case access_data : true

                

                    case update_destination_portal : true

                

                    case approve_ai_recommendations : true

                

                    case update_duration_of_user_block : true

                

                    case update_number_of_council_participants : true

                

                    case request_ddmo_change : true

                

                    case ddmo_council_voting_right : true

                

                    case ddmo_council_proposal_right : true

                

                    otherwise false

                endswitch

            

            otherwise false

        endswitch



    function aggregationRole ($e in Entity) =

	    if type($e) = ROLE then

            

	        switch $e

                

                    

                

                    

                case magister : ddmo_board_member

                    

                

                    

                case host : ddmo_member

                    

                

                    

                case analyst : ddmo_member

                    

                

                    

                case worker : ddmo_member

                    

                

                    

                case student : ddmo_member

                    

                

                    

                case ddmo_board_member : ddmo_member

                    

                

                    

                case freelancer : ddmo_member

                    

                

                    

                case institutional_representative : ddmo_board_member

                    

                

                    

                case mentor : ddmo_board_member

                    

                

                    

                

	            otherwise undef

	        endswitch

            

        endif

        

    function aggregationCommittee ($e in Entity) =

        if type($e) = COMMITTEE then

            

        	switch $e

                

                    

                

	            otherwise undef

	        endswitch

            

       	endif



    function roles ($u in User) = 

        switch $u 

            case owner : owner_role

            

        endswitch

        

    function type ($e in Entity) =

        switch $e

            

                

            case ddmo_council : COMMITTEE

                

            otherwise ROLE

            

        endswitch

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

    

    static advisor : Entity

    

    static founder : Entity

    

    static master_node : Entity

    

    static marketing_delegate : Entity

    

    static investor : Entity

    

    static developer : Entity

    

    static ambassador : Entity

    

    static dao_member : Entity

    

    static travelhive_daoowner : Entity

    

    static owner_role : Entity // for owner - controls all the roles - has all the permissions



    // Committees

    

    static dao_council : Entity

    

    static marketing_board : Entity

    

    static financial_board : Entity

    

    static travelware_board : Entity

    

    static development_board : Entity

    

    // Permissions

    

    static modify_salary_distribution_policy : Entity

    

    static upgrade_platform_feature : Entity

    

    static transfer_tokens : Entity

    

    static approve_project_budget : Entity

    

    static cut_project_funding : Entity

    

    static modify_salary_distribution_policy : Entity

    

    static supply_service : Entity

    

    static execute_task : Entity

    

    static assign_task : Entity

    

    static post_event : Entity

    

    static verify_institutional_profile : Entity

    

    static appoint_destination_committee : Entity

    

    static create_new_ddmo : Entity

    

    static propose_campaign_budget : Entity

    

    static veto_proposal : Entity

    

    static apply_for_governance_role : Entity

    

    static activate_role_delegation : Entity

    

    static request_task_delegation : Entity

    

    static dao_council_voting_right : Entity

    

    static dao_council_proposal_right : Entity

    

    static marketing_board_voting_right : Entity

    

    static marketing_board_proposal_right : Entity

    

    static financial_board_voting_right : Entity

    

    static financial_board_proposal_right : Entity

    

    static travelware_board_voting_right : Entity

    

    static travelware_board_proposal_right : Entity

    

    static development_board_voting_right : Entity

    

    static development_board_proposal_right : Entity

       



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

            

            case dao_council :

                false

            

            case marketing_board :

                false

            

            case financial_board :

                false

            

            case travelware_board :

                false

            

            case development_board :

                false

            



            case owner_role : 

                switch $control

                    

                    case advisor : true

                    

                    case founder : true

                    

                    case master_node : true

                    

                    case marketing_delegate : true

                    

                    case investor : true

                    

                    case developer : true

                    

                    case ambassador : true

                    

                    case dao_member : true

                    

                    case travelhive_daoowner : true

                    

                    

                    case dao_council : true

                    

                    case marketing_board : true

                    

                    case financial_board : true

                    

                    case travelware_board : true

                    

                    case development_board : true

                    

                    otherwise false

                endswitch



            

            case advisor :

                false

            

            case founder :

                false

            

            case master_node :

                false

            

            case marketing_delegate :

                false

            

            case investor :

                false

            

            case developer :

                false

            

            case ambassador :

                false

            

            case dao_member :

                false

            

            case travelhive_daoowner :

                false

            

            otherwise false

        endswitch



    function associate($e in Entity, $p in Permission) = 

        switch $e

            

                

            case advisor :

                switch $p

                    

                    case veto_proposal : true

                    

                    case travelware_board_voting_right : true

                    

                    case travelware_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case founder :

                switch $p

                    

                    case veto_proposal : true

                    

                    case travelware_board_voting_right : true

                    

                    case travelware_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case master_node :

                switch $p

                    

                    case development_board_voting_right : true

                    

                    case development_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case marketing_delegate :

                switch $p

                    

                    case post_event : true

                    

                    case marketing_board_voting_right : true

                    

                    case marketing_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case investor :

                switch $p

                    

                    case financial_board_voting_right : true

                    

                    case financial_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case developer :

                switch $p

                    

                    case development_board_voting_right : true

                    

                    case development_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case ambassador :

                switch $p

                    

                    case appoint_destination_committee : true

                    

                    case verify_institutional_profile : true

                    

                    case marketing_board_voting_right : true

                    

                    case marketing_board_proposal_right : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case dao_member :

                switch $p

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case apply_for_governance_role : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

                

            case travelhive_daoowner :

                switch $p

                    

                    case modify_salary_distribution_policy : true

                    

                    case upgrade_platform_feature : true

                    

                    case transfer_tokens : true

                    

                    case approve_project_budget : true

                    

                    case cut_project_funding : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case supply_service : true

                    

                    case execute_task : true

                    

                    case assign_task : true

                    

                    case post_event : true

                    

                    case verify_institutional_profile : true

                    

                    case appoint_destination_committee : true

                    

                    case create_new_ddmo : true

                    

                    case propose_campaign_budget : true

                    

                    case veto_proposal : true

                    

                    case apply_for_governance_role : true

                    

                    case activate_role_delegation : true

                    

                    case request_task_delegation : true

                    

                    case dao_council_voting_right : true

                    

                    case dao_council_proposal_right : true

                    

                    case marketing_board_voting_right : true

                    

                    case marketing_board_proposal_right : true

                    

                    case financial_board_voting_right : true

                    

                    case financial_board_proposal_right : true

                    

                    case travelware_board_voting_right : true

                    

                    case travelware_board_proposal_right : true

                    

                    case development_board_voting_right : true

                    

                    case development_board_proposal_right : true

                    

                    otherwise false

                endswitch

                

            

            

            

                

            case dao_council :

                switch $p

                    

                    case modify_salary_distribution_policy : true

                    

                    case upgrade_platform_feature : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case create_new_ddmo : true

                    

                    case activate_role_delegation : true

                    

                    otherwise false

                endswitch

                

            

                

            case marketing_board :

                switch $p

                    

                    case propose_campaign_budget : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case upgrade_platform_feature : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case create_new_ddmo : true

                    

                    case activate_role_delegation : true

                    

                    otherwise false

                endswitch

                

            

                

            case financial_board :

                switch $p

                    

                    case approve_project_budget : true

                    

                    case transfer_tokens : true

                    

                    case cut_project_funding : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case upgrade_platform_feature : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case create_new_ddmo : true

                    

                    case activate_role_delegation : true

                    

                    otherwise false

                endswitch

                

            

                

            case travelware_board :

                switch $p

                    

                    case assign_task : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case upgrade_platform_feature : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case create_new_ddmo : true

                    

                    case activate_role_delegation : true

                    

                    otherwise false

                endswitch

                

            

                

            case development_board :

                switch $p

                    

                    case upgrade_platform_feature : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case modify_salary_distribution_policy : true

                    

                    case create_new_ddmo : true

                    

                    case activate_role_delegation : true

                    

                    otherwise false

                endswitch

                

            



            case owner_role : 

                switch $p

                

                    case modify_salary_distribution_policy : true

                

                    case upgrade_platform_feature : true

                

                    case transfer_tokens : true

                

                    case approve_project_budget : true

                

                    case cut_project_funding : true

                

                    case modify_salary_distribution_policy : true

                

                    case supply_service : true

                

                    case execute_task : true

                

                    case assign_task : true

                

                    case post_event : true

                

                    case verify_institutional_profile : true

                

                    case appoint_destination_committee : true

                

                    case create_new_ddmo : true

                

                    case propose_campaign_budget : true

                

                    case veto_proposal : true

                

                    case apply_for_governance_role : true

                

                    case activate_role_delegation : true

                

                    case request_task_delegation : true

                

                    case dao_council_voting_right : true

                

                    case dao_council_proposal_right : true

                

                    case marketing_board_voting_right : true

                

                    case marketing_board_proposal_right : true

                

                    case financial_board_voting_right : true

                

                    case financial_board_proposal_right : true

                

                    case travelware_board_voting_right : true

                

                    case travelware_board_proposal_right : true

                

                    case development_board_voting_right : true

                

                    case development_board_proposal_right : true

                

                    otherwise false

                endswitch

            

            otherwise false

        endswitch



    function aggregationRole ($e in Entity) =

	    if type($e) = ROLE then

            

	        switch $e

                

                    

                case advisor : dao_member

                    

                

                    

                case founder : dao_member

                    

                

                    

                case master_node : dao_member

                    

                

                    

                case marketing_delegate : dao_member

                    

                

                    

                case investor : dao_member

                    

                

                    

                case developer : dao_member

                    

                

                    

                case ambassador : dao_member

                    

                

                    

                

                    

                

	            otherwise undef

	        endswitch

            

        endif

        

    function aggregationCommittee ($e in Entity) =

        if type($e) = COMMITTEE then

            

        	switch $e

                

                    

                

                    

                case marketing_board : dao_council

                    

                

                    

                case financial_board : dao_council

                    

                

                    

                case travelware_board : dao_council

                    

                

                    

                case development_board : dao_council

                    

                

	            otherwise undef

	        endswitch

            

       	endif



    function into ($p in Permission) = 

        

        switch $p

            

            case modify_salary_distribution_policy : None

            

            case upgrade_platform_feature : None

            

            case transfer_tokens : None

            

            case approve_project_budget : None

            

            case cut_project_funding : None

            

            case modify_salary_distribution_policy : None

            

            case supply_service : None

            

            case execute_task : None

            

            case assign_task : None

            

            case post_event : None

            

            case verify_institutional_profile : None

            

            case appoint_destination_committee : None

            

            case create_new_ddmo : None

            

            case propose_campaign_budget : None

            

            case veto_proposal : None

            

            case apply_for_governance_role : None

            

            case activate_role_delegation : None

            

            case request_task_delegation : None

            

            case dao_council_voting_right : None

            

            case dao_council_proposal_right : None

            

            case marketing_board_voting_right : None

            

            case marketing_board_proposal_right : None

            

            case financial_board_voting_right : None

            

            case financial_board_proposal_right : None

            

            case travelware_board_voting_right : None

            

            case travelware_board_proposal_right : None

            

            case development_board_voting_right : None

            

            case development_board_proposal_right : None

            

        endswitch

        



    function roles ($u in User) = 

        switch $u 

            case owner : owner_role

            

        endswitch

        

    function type ($e in Entity) =

        switch $e

            

                

            case dao_council : COMMITTEE

                

            case marketing_board : COMMITTEE

                

            case financial_board : COMMITTEE

                

            case travelware_board : COMMITTEE

                

            case development_board : COMMITTEE

                

            otherwise ROLE

            

        endswitch

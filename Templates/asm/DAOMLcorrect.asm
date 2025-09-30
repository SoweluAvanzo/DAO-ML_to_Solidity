/*
Complete Model : 
    The complete DAO-ML model, it implements : 
    - All the permissions
    - All the roles/committees
    - Actors
    - Governance Areas

    - Control relations
    - Association Relation
    - Aggregation Relation
    - Into relation (associates permissions inside governance areas)
    - Roles to Actors association
    - Entity type (ROLE, COMMITTEE)

    - Supported operations : (ASSIGNROLE, REVOKEROLE, GRANTPERM, REVOKEPERM)

    The Permission and Control association inheritance is checked through recursive derived functions (Not supported by NuSMV)
*/


asm DAOMLcorrect

import ../lib/StandardLibrary

signature : 
    abstract domain User
    abstract domain Permission
    abstract domain Entity
    abstract domain GovernanceArea
    enum domain EntityType = {ROLE, COMMITTEE}
    enum domain Operation = {ASSIGNROLE, REVOKEROLE, GRANTPERM, REVOKEPERM}

	
    controlled controls : Prod(Entity, Entity) -> Boolean
    
    controlled associate : Prod(Entity, Permission) -> Boolean

    controlled aggregationRole : Entity -> Entity
    controlled aggregationCommittee : Entity -> Entity

    controlled into : Permission -> GovernanceArea

    controlled roles : User -> Entity

    controlled type : Entity -> EntityType

    // Roles
    static worker : Entity
    static freelancer : Entity
    static host : Entity
    static ddmo_member : Entity
    static ddmo_board_member : Entity
    static magister : Entity
    static institutional_representative : Entity
    static student : Entity
    static analyst : Entity
    static mentor : Entity
    
    static owner_role : Entity // for owner - controls all the roles - has all the permissions

    // Committees
    static ddmo_council : Entity

    // Permissions
    static supply_service : Permission
    static propose_task_delegation : Permission
    static execute_task : Permission
    static share_task : Permission

    static request_ddmo_change : Permission

    static report_task_unaccomplishment : Permission
    static block_user : Permission
    static trigger_dispute_resolution : Permission
    static oversee_dispute : Permission
    static approve_kyb : Permission
    static resolve_dispute : Permission

    static access_data : Permission
    static update_destination_portal : Permission
    static approve_ai_recommendations : Permission

    static update_duration_user_block : Permission
    static update_number_council_partecipants : Permission

    static suspend_ddmo : Permission
    static liquidate_ddmo : Permission
    static merge_ddmo : Permission
    
    

    // Governance Areas
    static task_execution : GovernanceArea
    static ddmo_membership : GovernanceArea
    static dispute_resolution : GovernanceArea
    static destination_data_manager : GovernanceArea
    static council_governance : GovernanceArea
    static ddmo_restructuring : GovernanceArea
    

    // Users
    static owner : User
    static user1 : User

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
                switch $control
                    case ddmo_board_member : true
                    otherwise false
                endswitch
            case owner_role : 
                switch $control
                    case worker : true
                    case freelancer : true
                    case host : true
                    case ddmo_member : true
                    case ddmo_board_member : true
                    case magister : true
                    case institutional_representative : true
                    case student : true
                    case analyst : true
                    case mentor : true
                    case ddmo_council : true
                    otherwise false
                endswitch
            otherwise false
        endswitch

    function associate($e in Entity, $p in Permission) = 
        switch $e
            case worker : 
                false
            case freelancer : 
                false
            case host : 
                false
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
                    case trigger_dispute_resolution : true
                    case oversee_dispute : true
                    case resolve_dispute : true
                    otherwise false
                endswitch
            case ddmo_board_member : 
                false
            case institutional_representative : 
                switch $p
                    case access_data : true
                    otherwise false
                endswitch
            case student : 
                switch $p
                    case access_data : true
                    otherwise false
                endswitch
            case analyst : 
                switch $p
                    case access_data : true
                    otherwise false
                endswitch
            case mentor : 
                switch $p
                    case approve_ai_recommendations : true
                    case approve_kyb : true
                    otherwise false
                endswitch
            case ddmo_council : 
                switch $p
                    case update_destination_portal : true
                    case update_duration_user_block : true
                    case update_number_council_partecipants : true
                    case suspend_ddmo : true
                    case liquidate_ddmo : true
                    case merge_ddmo : true
                    otherwise false
                endswitch
             case owner_role : // owner has all permissions
                switch $p
                	case approve_ai_recommendations : true
                    case approve_kyb : true
                	case access_data : true
                	case supply_service : true
                    case propose_task_delegation : true
                    case execute_task : true
                    case share_task : true
                    case request_ddmo_change : true
                	case block_user : true
                    case trigger_dispute_resolution : true
                    case oversee_dispute : true
                    case resolve_dispute : true
                    case report_task_unaccomplishment : true
                    case update_destination_portal : true
                    case update_duration_user_block : true
                    case update_number_council_partecipants : true
                    case suspend_ddmo : true
                    case liquidate_ddmo : true
                    case merge_ddmo : true
                    otherwise false
                endswitch
            otherwise false
        endswitch

    function aggregationRole ($e in Entity) =
	    if type($e) = ROLE then
	        switch $e
	            case worker : ddmo_member
	            case freelancer : ddmo_member
	            case host : ddmo_member
	            case student : ddmo_member
	            case analyst : ddmo_member
	            case ddmo_member : ddmo_board_member
	            case magister : ddmo_board_member
	            case institutional_representative : ddmo_board_member
	            case mentor : ddmo_board_member
	            otherwise undef
	        endswitch
	     endif
        
    function aggregationCommittee ($e in Entity) =
        if type($e) = COMMITTEE then
        	undef
       	endif

    function into ($p in Permission) = 
        switch $p
            case supply_service : task_execution
            case propose_task_delegation : task_execution
            case execute_task : task_execution
            case share_task : task_execution
            case request_ddmo_change : ddmo_membership
            case report_task_unaccomplishment : dispute_resolution
            case block_user : dispute_resolution
            case trigger_dispute_resolution : dispute_resolution
            case oversee_dispute : dispute_resolution
            case approve_kyb : dispute_resolution
            case resolve_dispute : dispute_resolution
            case access_data : destination_data_manager
            case update_destination_portal : destination_data_manager
            case approve_ai_recommendations : destination_data_manager
            case update_duration_user_block : council_governance
            case update_number_council_partecipants : council_governance
            case suspend_ddmo : ddmo_restructuring
            case liquidate_ddmo : ddmo_restructuring
            case merge_ddmo : ddmo_restructuring
        endswitch

    function roles ($u in User) = 
        switch $u 
            case owner : owner_role
        endswitch
        
    function type ($e in Entity) =
        switch $e
            case ddmo_council : COMMITTEE
            otherwise ROLE
        endswitch

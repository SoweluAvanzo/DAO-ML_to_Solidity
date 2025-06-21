
parser grammar XMLParser;

options {
    tokenVocab = XMLLexer;
}

document
    : prolog? misc* diagram misc* EOF
    ;

prolog
    : XMLDeclOpen attribute* SPECIAL_CLOSE
    ;

content
    : chardata? ((element | reference | comments_and_stuff) chardata?)*
    ;
element
    : '<' Name attribute* '>' content '<' '/' Name '>'
    | '<' Name attribute* '/>'
    ;


diagram: OPEN DIAGRAM misc* attribute* misc* CLOSE chardata? ((dao | reference | comments_and_stuff | attribute) misc* chardata?)* OPEN SLASH DIAGRAM CLOSE
    ;

dao
    :  OPEN DAO misc* ((dao_id | dao_name | mission_statement | hierarchical_inheritance | comments_and_stuff | attribute) misc* )* CLOSE daocontent OPEN SLASH DAO CLOSE
    ;

role
    : OPEN ROLE misc* ((role_id | role_name | role_assignment_method | n_agent_min | n_agent_max | agent_type | aggregation_level | federation_level | comments_and_stuff | attribute) misc* )* CLOSE relations OPEN SLASH ROLE CLOSE
    ;

committee
    : OPEN COMMITTEE misc* ((committee_id | committee_description | voting_condition | proposal_condition | decision_making_method | aggregation_level | federation_level | comments_and_stuff | attribute) misc* )* CLOSE relations OPEN SLASH COMMITTEE CLOSE
    ;

permission
    : OPEN PERMISSION  misc* ((permission_id | allowed_action | permission_type | ref_gov_area | comments_and_stuff | attribute) misc* )* SLASH_CLOSE
    ;

gov
    : OPEN GOV set_of_attributes SLASH_CLOSE
    ;

daocontent
    : chardata? ((role | committee | permission | gov | reference | comments_and_stuff) chardata?)*
    ;

relations
        : chardata? ((associated_to | controlled_by | aggregates | federates_into | COMMENT) chardata?)*
        ;
    
associated_to: OPEN ASSOCIATION set_of_attributes CLOSE content OPEN SLASH ASSOCIATION CLOSE
    ;

controlled_by: OPEN CONTROL set_of_attributes CLOSE content OPEN SLASH CONTROL CLOSE
    ;

aggregates: OPEN AGGREGATES set_of_attributes CLOSE content OPEN SLASH AGGREGATES CLOSE
    ;

federates_into: OPEN FEDERATES set_of_attributes CLOSE content OPEN SLASH FEDERATES CLOSE
    ;

reference
    : EntityRef
    | CharRef
    ;

comments_and_stuff : CDATA | PI | COMMENT;
set_of_attributes : misc* ((comments_and_stuff | attribute) misc* )* ;

// DAO attributes
dao_id : DAOID EQUALS STRING ;
dao_name : DAONAME EQUALS STRING ;
mission_statement : MISSIONSTATEMENT EQUALS STRING ;
hierarchical_inheritance : HIERARCHICALINHERITANCE EQUALS STRING ;

// Role attributes
role_id : ROLEID EQUALS STRING ;
role_name : ROLENAME EQUALS STRING ;
role_assignment_method : ROLEASSIGNMENTMETHOD EQUALS STRING ;
n_agent_min : NAGENTMIN EQUALS STRING;
n_agent_max : NAGENTMAX EQUALS STRING ;
agent_type : AGENTTYPE EQUALS STRING;

// Committee attributes
committee_id : COMMITTEEID EQUALS STRING ;
committee_description : COMMITTEEDESCRIPTION EQUALS STRING ;
voting_condition : VOTINGCONDITION EQUALS STRING ;
proposal_condition : PROPOSALCONDITION EQUALS STRING ;
decision_making_method : DMMETHOD EQUALS STRING ;
aggregation_level : AGGREGATIONLEVEL EQUALS STRING;
federation_level : FEDERATIONLEVEL EQUALS STRING;

// Permission attributes
permission_id : PERMISSIONID EQUALS STRING ;
allowed_action : ALLOWEDACTION EQUALS STRING ;
permission_type: PERMISSIONTYPE EQUALS STRING;
ref_gov_area : REF_GOV_AREA EQUALS STRING; 

//generic attribute definition
attribute
    : Name '=' STRING
    ; // Our STRING is AttValue in spec

/** ``All text that is not markup constitutes the character data of
 *  the document.''
 */
chardata
    : TEXT
    | SEA_WS
    ;

misc
    : COMMENT
    | PI
    | SEA_WS
    ;
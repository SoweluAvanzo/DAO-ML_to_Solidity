
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
    : chardata? ((element | reference | CDATA | PI | COMMENT) chardata?)*
    ;
element
    : '<' Name attribute* '>' content '<' '/' Name '>'
    | '<' Name attribute* '/>'
    ;


diagram: OPEN DIAGRAM misc* attribute* misc* CLOSE chardata? ((dao | reference | CDATA | PI | COMMENT) chardata?)* OPEN SLASH DIAGRAM CLOSE
    ;

dao
    :  OPEN DAO misc* dao_id misc* dao_name misc* mission_statement misc* hierarchical_inheritance misc* CLOSE daocontent OPEN SLASH DAO CLOSE
    ;

role
    : OPEN ROLE misc* role_id misc* role_name misc* role_assignment_method? misc* n_agent_min? misc* n_agent_max? misc* agent_type misc* aggregation_level? misc* federation_level? misc* CLOSE relations OPEN SLASH ROLE CLOSE
    ;

committee
    : OPEN COMMITTEE committee_id misc* committee_description misc* voting_condition? misc* proposal_condition? misc* decision_making_method? misc* aggregation_level? misc* federation_level? misc* CLOSE relations OPEN SLASH COMMITTEE CLOSE
    ;

permission
    : OPEN PERMISSION permission_id misc* allowed_action misc* permission_type misc* ref_gov_area? misc* SLASH_CLOSE
    ;

gov
    : OPEN GOV attribute* SLASH_CLOSE
    ;

daocontent
    : chardata? ((role | committee | permission | gov | reference | CDATA | PI | COMMENT) chardata?)*
    ;


relations
        : chardata? ((associated_to | controlled_by | aggregates | federates_into | COMMENT) chardata?)*
        ;
    
associated_to: OPEN ASSOCIATION attribute* CLOSE content OPEN SLASH ASSOCIATION CLOSE
    ;

controlled_by: OPEN CONTROL attribute* CLOSE content OPEN SLASH CONTROL CLOSE
    ;

aggregates: OPEN AGGREGATES attribute* CLOSE content OPEN SLASH AGGREGATES CLOSE
    ;

federates_into: OPEN FEDERATES attribute* CLOSE content OPEN SLASH FEDERATES CLOSE
    ;

reference
    : EntityRef
    | CharRef
    ;

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
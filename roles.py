import pandas as pd


allRoles = pd.read_excel('C:/Users/gamelo/Desktop/gerador_vuser2/data/Roles.xlsx')
chemicalMarket = allRoles[['Business','Chemicals']].copy()
chemicalPricing = allRoles[['Business','Chemicals.1','Chemicals.2','Chemicals.3','Chemicals.4','Chemicals.5']].copy()
chemicalCommercial = allRoles[['Business','Chemicals.6','Chemicals.7','Chemicals.8','Chemicals.9','Chemicals.10','Chemicals.11','Chemicals.12','Chemicals.13']].copy()
polymersMarket = allRoles[['Business','Polymers','Polymers.1','Polymers.2','Polymers.3']].copy()
polymersPricing = allRoles[['Business','Polymers.4','Polymers.5','Polymers.6','Polymers.7']].copy()
polymersCommercial = allRoles[['Business','Polymers.8','Polymers.9','Polymers.10','Polymers.11','Polymers.12','Polymers.13','Polymers.14','Polymers.15','Polymers.16']].copy()
polymersCustomerService = allRoles[['Business','Polymers.17','Polymers.18','Polymers.19']].copy()

chemicalMarket.columns=chemicalMarket.iloc[1]
chemicalMarket = chemicalMarket.drop(chemicalMarket.index[[0,1]])

chemicalPricing.columns=chemicalPricing.iloc[1]
chemicalPricing = chemicalPricing.drop(chemicalPricing.index[[0,1]])

chemicalCommercial.columns=chemicalCommercial.iloc[1]
chemicalCommercial = chemicalCommercial.drop(chemicalCommercial.index[[0,1]])

polymersMarket.columns=polymersMarket.iloc[1]
polymersMarket = polymersMarket.drop(polymersMarket.index[[0,1]])

polymersPricing.columns=polymersPricing.iloc[1]
polymersPricing = polymersPricing.drop(polymersPricing.index[[0,1]])

polymersCommercial.columns=polymersCommercial.iloc[1]
polymersCommercial = polymersCommercial.drop(polymersCommercial.index[[0,1]])

polymersCustomerService.columns=polymersCustomerService.iloc[1]
polymersCustomerService = polymersCustomerService.drop(polymersCustomerService.index[[0,1]])

VRoleXML = '\n            <VRole>'
VRoleXMLEnd = '</VRole>'
#Initial Chemicals
def marketingIntelligenceChemicals():
    chemicalMarketf = chemicalMarket['Business Position'].loc[chemicalMarket['MarketingIntelligence'].notnull()]
    rolesMarketingIntelligenceChemicals = ''
    for elem in chemicalMarketf:
        rolesMarketingIntelligenceChemicals = rolesMarketingIntelligenceChemicals + VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesMarketingIntelligenceChemicals
    return roleXML

def pricingInternChemicals():
    pricingIntern = chemicalPricing['Business Position'].loc[chemicalPricing['PricingIntern'].notnull()]
    rolesPricingInternChemicals = ''
    for elem in pricingIntern:
        rolesPricingInternChemicals = rolesPricingInternChemicals +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingInternChemicals
    return roleXML

def pricingAnalystChemicals():
    PricingAnalyst = chemicalPricing['Business Position'].loc[chemicalPricing['PricingAnalyst'].notnull()]
    rolesPricingAnalystChemicals = ''
    for elem in PricingAnalyst:
        rolesPricingAnalystChemicals = rolesPricingAnalystChemicals +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingAnalystChemicals
    return roleXML

def pricingCoordinatorChemicals():
    PricingCoordinator = chemicalPricing['Business Position'].loc[chemicalPricing['PricingCoordinator'].notnull()]
    rolesPricingCoordinatorChemical = ''
    for elem in PricingCoordinator:
        rolesPricingCoordinatorChemical = rolesPricingCoordinatorChemical +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingCoordinatorChemical
    return roleXML

def pricingManagerChemicals():
    pricingManager = chemicalPricing['Business Position'].loc[chemicalPricing['PricingManager'].notnull()]
    rolesPricingManagerChemicals = ''
    for elem in pricingManager:
        rolesPricingManagerChemicals = rolesPricingManagerChemicals +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingManagerChemicals
    return roleXML

def pricingDirectorChemicals():
    pricingDirector = chemicalPricing['Business Position'].loc[chemicalPricing['PricingDirector'].notnull()]
    rolesPricingDirectorChemicals = ''
    for elem in pricingDirector:
        rolesPricingDirectorChemicals = rolesPricingDirectorChemicals +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingDirectorChemicals
    return roleXML

def commercialInternChemicals():
    commercialIntern = chemicalCommercial['Business Position'].loc[chemicalCommercial['CommercialIntern'].notnull()]
    rolesCommercialInternChemicals = ''
    for elem in commercialIntern:
        rolesCommercialInternChemicals = rolesCommercialInternChemicals +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialInternChemicals
    return roleXML

def exportBackofficeCoordinatorChemicals():
    exportBackofficeCoordinator = chemicalCommercial['Business Position'].loc[chemicalCommercial['ExportBackofficeCoordinator'].notnull()]
    rolesCommercialExportBackofficeCoordinator = ''
    for elem in exportBackofficeCoordinator:
        rolesCommercialExportBackofficeCoordinator = rolesCommercialExportBackofficeCoordinator +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialExportBackofficeCoordinator
    return roleXML

def backofficemanagerChemicals():
    backofficemanager = chemicalCommercial['Business Position'].loc[chemicalCommercial['Backofficemanager'].notnull()]
    rolesCommercialBackofficemanager = ''
    for elem in backofficemanager:
        rolesCommercialBackofficemanager = rolesCommercialBackofficemanager +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialBackofficemanager
    return roleXML

def commercialCommercialAnalystChemicals():
    commercialAnalyst = chemicalCommercial['Business Position'].loc[chemicalCommercial['CommercialAnalyst'].notnull()]
    rolesCommercialCommercialAnalyst = ''
    for elem in commercialAnalyst:
        rolesCommercialCommercialAnalyst = rolesCommercialCommercialAnalyst +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialAnalyst
    return roleXML

def commercialAccountManagerChemicals():
    commercialAccountManager = chemicalCommercial['Business Position'].loc[chemicalCommercial['CommercialAccountManager'].notnull()]
    rolesCommercialCommercialAccountManager = ''
    for elem in commercialAccountManager:
        rolesCommercialCommercialAccountManager = rolesCommercialCommercialAccountManager +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialAccountManager
    return roleXML

def commercialCommercialManagerChemicals():
    commercialManager = chemicalCommercial['Business Position'].loc[chemicalCommercial['CommercialManager'].notnull()]
    rolesCommercialCommercialManager = ''
    for elem in commercialManager:
        rolesCommercialCommercialManager = rolesCommercialCommercialManager +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialManager
    return roleXML

def commercialCommercialDirectorChemicals():
    commercialDirector = chemicalCommercial['Business Position'].loc[chemicalCommercial['CommercialDirector'].notnull()]
    rolesCommercialCommercialDirector = ''
    for elem in commercialDirector:
        rolesCommercialCommercialDirector = rolesCommercialCommercialDirector +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialDirector
    return roleXML

def commercialVPChemicals():
    VP = chemicalCommercial['Business Position'].loc[chemicalCommercial['VP'].notnull()]
    rolesCommercialVP = ''
    for elem in VP:
        rolesCommercialVP = rolesCommercialVP +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialVP
    return roleXML

#Initial Polymers
def marketingIntelligencePolymers():
    polymersMarketf = polymersMarket['Business Position'].loc[polymersMarket['MarketingIntelligence'].notnull()]
    rolesMarketingIntelligencePolymers = ''
    for elem in polymersMarketf:
        rolesMarketingIntelligencePolymers = rolesMarketingIntelligencePolymers +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesMarketingIntelligencePolymers
    return roleXML

def marketingInternPolymers():
    marketingIntern = polymersMarket['Business Position'].loc[polymersMarket['MarketingIntern'].notnull()]
    rolesMarketingInternPolymers = ''
    for elem in marketingIntern:
        rolesMarketingInternPolymers = rolesMarketingInternPolymers +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesMarketingInternPolymers
    return roleXML

def marketingMarketingStrategy():
    marketingStrategy = polymersMarket['Business Position'].loc[polymersMarket['Marketing&Strategy'].notnull()]
    rolesMarketingStrategy = ''
    for elem in marketingStrategy:
        rolesMarketingStrategy = rolesMarketingStrategy +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesMarketingStrategy
    return roleXML

def marketingMarketingAnalyst():
    marketingAnalyst = polymersMarket['Business Position'].loc[polymersMarket['MarketingAnalyst'].notnull()]
    rolesMarketingAnalyst = ''
    for elem in marketingAnalyst:
        rolesMarketingAnalyst = rolesMarketingAnalyst +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesMarketingAnalyst
    return roleXML

def pricingInternPolymers():
    pricingIntern = polymersPricing['Business Position'].loc[polymersPricing['PricingIntern'].notnull()]
    rolesPricingInternPolymers = ''
    for elem in pricingIntern:
        rolesPricingInternPolymers = rolesPricingInternPolymers +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingInternPolymers
    return roleXML

def pricingAnalystPolymers():
    PricingAnalyst = polymersPricing['Business Position'].loc[polymersPricing['PricingAnalyst'].notnull()]
    rolesPricingAnalystPolymers = ''
    for elem in PricingAnalyst:
        rolesPricingAnalystPolymers = rolesPricingAnalystPolymers +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingAnalystPolymers
    return roleXML

def pricingCoordinatorPolymers():
    PricingCoordinator = polymersPricing['Business Position'].loc[polymersPricing['PricingCoordinator'].notnull()]
    rolesPricingCoordinatorChemical = ''
    for elem in PricingCoordinator:
        rolesPricingCoordinatorChemical = rolesPricingCoordinatorChemical +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingCoordinatorChemical
    return roleXML

def pricingManagerPolymers():
    pricingManager = polymersPricing['Business Position'].loc[polymersPricing['PricingManager'].notnull()]
    rolesPricingManagerPolymers = ''
    for elem in pricingManager:
        rolesPricingManagerPolymers = rolesPricingManagerPolymers +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPricingManagerPolymers
    return roleXML

def commercialInternPolymers():
    commercialIntern = polymersCommercial['Business Position'].loc[polymersCommercial['CommercialIntern'].notnull()]
    rolesCommercialInternPolymers = ''
    for elem in commercialIntern:
        rolesCommercialInternPolymers = rolesCommercialInternPolymers +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialInternPolymers
    return roleXML

def commercialCommercialAnalystPolymers():
    commercialAnalyst = polymersCommercial['Business Position'].loc[polymersCommercial['CommercialAnalyst'].notnull()]
    rolesCommercialCommercialAnalyst = ''
    for elem in commercialAnalyst:
        rolesCommercialCommercialAnalyst = rolesCommercialCommercialAnalyst +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialAnalyst
    return roleXML

def commercialAccountManagerPolymers():
    commercialAccountManager = polymersCommercial['Business Position'].loc[polymersCommercial['CommercialAccountManager'].notnull()]
    rolesCommercialCommercialAccountManager = ''
    for elem in commercialAccountManager:
        rolesCommercialCommercialAccountManager = rolesCommercialCommercialAccountManager +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialAccountManager
    return roleXML

def commercialCommercialManager():
    commercialManager = polymersCommercial['Business Position'].loc[polymersCommercial['CommercialManager'].notnull()]
    rolesCommercialCommercialManager = ''
    for elem in commercialManager:
        rolesCommercialCommercialManager = rolesCommercialCommercialManager +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialManager
    return roleXML

def commercialCommercialDirector():
    commercialDirector = polymersCommercial['Business Position'].loc[polymersCommercial['CommercialDirector'].notnull()]
    rolesCommercialCommercialDirector = ''
    for elem in commercialDirector:
        rolesCommercialCommercialDirector = rolesCommercialCommercialDirector +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialCommercialDirector
    return roleXML

def commercialVP():
    VP = polymersCommercial['Business Position'].loc[polymersCommercial['VP'].notnull()]
    rolesCommercialVP = ''
    for elem in VP:
        rolesCommercialVP = rolesCommercialVP +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialVP
    return roleXML

def commercialGAC():
    GAC = polymersCommercial['Business Position'].loc[polymersCommercial['GAC'].notnull()]
    rolesCommercialGAC = ''
    for elem in GAC:
        rolesCommercialGAC = rolesCommercialGAC +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialGAC
    return roleXML

def commercialBusinessDirector():
    businessDirector = polymersCommercial['Business Position'].loc[polymersCommercial['BusinessDirector'].notnull()]
    rolesCommercialBusinessDirector= ''
    for elem in businessDirector:
        rolesCommercialBusinessDirector = rolesCommercialBusinessDirector +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCommercialBusinessDirector
    return roleXML

def commercialPerformanceManagement():
    performanceManagement = polymersCommercial['Business Position'].loc[polymersCommercial['PerformanceManagement'].notnull()]
    rolesPerformanceManagement= ''
    for elem in performanceManagement:
        rolesPerformanceManagement = rolesPerformanceManagement +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesPerformanceManagement
    return roleXML

def customerServiceDirector():
    customerServiceDirectorf = polymersCustomerService['Business Position'].loc[polymersCustomerService['CustomerServiceDirector'].notnull()]
    rolesCustomerServiceDirector= ''
    for elem in customerServiceDirectorf:
        rolesCustomerServiceDirector = rolesCustomerServiceDirector +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCustomerServiceDirector
    return roleXML

def customerServiceTeam():
    customerServiceTeamf = polymersCustomerService['Business Position'].loc[polymersCustomerService['CustomerServiceTeam'].notnull()]
    rolesCustomerServiceTeam= ''
    for elem in customerServiceTeamf:
        rolesCustomerServiceTeam = rolesCustomerServiceTeam +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCustomerServiceTeam
    return roleXML

def customerServiceLeader():
    customerServiceLeaderf = polymersCustomerService['Business Position'].loc[polymersCustomerService['CustomerServiceLeader'].notnull()]
    rolesCustomerServiceLeader= ''
    for elem in customerServiceLeaderf:
        rolesCustomerServiceLeader = rolesCustomerServiceLeader +VRoleXML + elem + VRoleXMLEnd
    roleXML = rolesCustomerServiceLeader
    return roleXML
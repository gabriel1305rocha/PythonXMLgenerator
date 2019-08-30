import pandas as pd
import math
import numpy as np
from roles import *

USER  = """
    <User>
        <Name>{user}</Name>
        <Password>{password}</Password>
        <FullName>{fullname}</FullName>
        <Email>{email}</Email>
        <alidity>01/01/2001..eot</alidity>
        <DefaultUOM>TO</DefaultUOM>
        <DefaultCurrency>BRL</DefaultCurrency>
        <EmployeeID>{employeeid}</EmployeeID>
        <ReportsTo>{reportTo}</ReportsTo>
        <Business>{business}</Business>
        <BusinessArea>{businessArea}</BusinessArea>
        <BusinessPosition>{businessPosition}</BusinessPosition>
        <Groups> 
            {groups}{SalesHierarchy}
            {setorA}
         </Groups>
        <Roles>
            {roleOK}
        </Roles>
        <IsSysAdmin>false</IsSysAdmin>
        <DefaultLocale>pt_BR</DefaultLocale>
    </User>
"""

MI  = """<Group>GeographyHierarchy-GeographyLeel3-Brazil~GeographyHierarchyGroup</Group>"""
ME  = """<Group>GeographyHierarchy-AE-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-AR-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-AT-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-AU-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-BD-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-BE-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-BG-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-BO-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-BS-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CA-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CH-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CL-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CN-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CO-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CR-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-CZ-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-DE-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-DK-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-DO-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-EC-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-EG-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-ES-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-FR-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-GB-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-GT-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-HK-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-HR-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-ID-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-IL-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-IN-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-IT-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-JO-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-JP-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-KR-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-LB-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-LT-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-LU-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-MA-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-MU-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-MX-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-MY-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-NL-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-NZ-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-PA-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-PE-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-PL-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-PT-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-PY-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-RU-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-SA-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-SE-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-SG-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-SI-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-SK-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-SV-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-TR-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-TW-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-US-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-UY-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-E-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-G-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-N-~GeographyHierarchyGroup</Group>
            <Group>GeographyHierarchy-ZA-~GeographyHierarchyGroup</Group>"""
SalesHierarchy  = """
            <Group>SalesHierarchy-SalesLeel1-BR10~SalesHierarchyGroup</Group>
            <Group>SalesHierarchy-SalesLeel2-BR10~SalesHierarchyGroup</Group>
            <Group>SalesHierarchy-SalesOrg-BR10~SalesHierarchyGroup</Group>"""
setorA21  = """<Group>SABR100121~SalesArea</Group>"""
setorA2122  = setorA21  + """\n            <Group>SABR100122~SalesArea</Group>"""
setorA27  = """<Group>SABR100127~SalesArea</Group>"""
setorA142  = """<Group>SABR100101~SalesArea</Group>
                <Group>SABR100104~SalesArea</Group>
                <Group>SABR100102~SalesArea</Group>"""
setorA1426  = setorA142  + """\n                <Group>SABR100106~SalesArea</Group>"""
setorA14263  = setorA1426  + """\n                <Group>SABR100103~SalesArea</Group>"""
setorA2526  = """<Group>SABR100125~SalesArea</Group>
                <Group>SABR100126~SalesArea</Group>"""
setorA142632526  = setorA14263  + "\n                "+setorA2526 
setorA146  = """<Group>SABR100101~SalesArea</Group>
                <Group>SABR100104~SalesArea</Group>
                <Group>SABR100106~SalesArea</Group>"""
setorA212227  = setorA2122  + "\n            "+setorA27 
setorA3  = """<Group>SABR100103~SalesArea</Group>"""

dados = pd.read_csv('./data/USERS.csv', sep=';')
output = open('./XML/user.xml ', 'w')

output.write("<entity-data>")

for row in dados.values:
      
   if not row[6] or pd.isnull(row[6]):
      row[6] = ''
   else:
      employeeid = (str(row[6]))
      employeeidAux = employeeid.split('.')
      employeeid = employeeidAux[0]

   if row[9] == 'MI':
      groups = MI
   elif row[9] == 'ME':
      groups = ME
   elif row[9] == 'MI /ME':
      groups = (MI+ME)

   user = row[1]
   password = '4657ifjkhollko@#tgdf87'
   fullname = row[0]
   email = row[2]
   if pd.isnull(row[7]):
      reportTo = ''
   else:
      reportTo = row[7]

   business = row[3]

   businessArea = row[4]
   if pd.isnull(row[5]):
      businessPosition = ''
   else:
      businessPosition = row[5]
   if (businessPosition == 'MarketingIntelligence' and businessArea == 'Marketing' and ('Chemicals' in business)):
      roleOK = marketingIntelligenceChemicals()
   elif (businessPosition == 'PricingIntern' and businessArea == 'Pricing' and ('Chemicals' in business)):
      roleOK = pricingInternChemicals()
   elif (businessPosition == 'PricingAnalyst' and businessArea == 'Pricing' and ('Chemicals' in business)):
      roleOK = pricingAnalystChemicals()
   elif (businessPosition == 'PricingCoordinator' and businessArea == 'Pricing' and ('Chemicals' in business)):
      roleOK = pricingCoordinatorChemicals()
   elif (businessPosition == 'PricingManager' and businessArea == 'Pricing' and ('Chemicals' in business)):
      roleOK = pricingManagerChemicals()
   elif (businessPosition == 'PricingDirector' and businessArea == 'Pricing' and ('Chemicals' in business)):
      roleOK = pricingDirectorChemicals()
   elif (businessPosition == 'CommercialIntern' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = commercialInternChemicals()
   elif (businessPosition == 'ExportBackofficeCoordinator' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = exportBackofficeCoordinatorChemicals()
   elif (businessPosition == 'Backofficemanager' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = backofficemanagerChemicals()
   elif (businessPosition == 'CommercialAnalyst' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = commercialCommercialAnalystChemicals()
   elif (businessPosition == 'CommercialAccountManager' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = commercialAccountManagerChemicals()
   elif (businessPosition == 'CommercialManager' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = commercialCommercialManagerChemicals()
   elif (businessPosition == 'CommercialDirector' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = commercialCommercialDirectorChemicals()
   elif (businessPosition == 'VP' and businessArea == 'Commercial' and ('Chemicals' in business)):
      roleOK = commercialVPChemicals()
   elif (businessPosition == 'MarketingIntelligence' and businessArea == 'Marketing' and ('Polymers' in business)):
      roleOK = marketingIntelligencePolymers()
   elif (businessPosition == 'MarketingIntern' and businessArea == 'Marketing' and ('Polymers' in business)):
      roleOK = marketingInternPolymers()
   elif (businessPosition == 'Marketing&Strategy' and businessArea == 'Marketing' and ('Polymers' in business)):
      roleOK = marketingMarketingStrategy()
   elif (businessPosition == 'MarketingAnalyst' and businessArea == 'Marketing' and ('Polymers' in business)):
      roleOK = marketingMarketingAnalyst()
   elif (businessPosition == 'PricingIntern' and businessArea == 'Pricing' and ('Polymers' in business)):
      roleOK = pricingInternPolymers()
   elif (businessPosition == 'PricingAnalyst' and businessArea == 'Pricing' and ('Polymers' in business)):
      roleOK = pricingAnalystPolymers()
   elif (businessPosition == 'PricingCoordinator' and businessArea == 'Pricing' and ('Polymers' in business)):
      roleOK = pricingCoordinatorPolymers()
   elif (businessPosition == 'PricingManager' and businessArea == 'Pricing' and ('Polymers' in business)):
      roleOK = pricingManagerPolymers()
   elif (businessPosition == 'CommercialIntern' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialInternPolymers()
   elif (businessPosition == 'CommercialAnalyst' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialCommercialAnalystPolymers()
   elif (businessPosition == 'GAC' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialGAC()
   elif (businessPosition == 'CommercialAccountManager' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialAccountManagerPolymers()
   elif (businessPosition == 'CommercialManager' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialCommercialManager()
   elif (businessPosition == 'CommercialDirector' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialCommercialDirector()
   elif (businessPosition == 'VP' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialVP()
   elif (businessPosition == 'BusinessDirector' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialBusinessDirector()
   elif (businessPosition == 'PerformanceManagement' and businessArea == 'Commercial' and ('Polymers' in business)):
      roleOK = commercialPerformanceManagement()
   elif (businessPosition == 'CustomerServiceDirector' and businessArea == 'CustomerServiceDirector' and ('Polymers' in business)):
      roleOK = customerServiceDirector()
   elif (businessPosition == 'CustomerServiceTeam' and businessArea == 'CustomerServiceDirector' and ('Polymers' in business)):
      roleOK = customerServiceTeam()
   elif (businessPosition == 'CustomerServiceLeader' and businessArea == 'CustomerServiceDirector' and ('Polymers' in business)):
      roleOK = customerServiceLeader()
   else:
      roleOK = ''
   st = str(row[8]).split(',')
   my_dict = {'21': setorA21, '21,22': setorA2122, 
               '25,26': setorA2526, '27': setorA27,
               '01,04,02': setorA142, '01,04,02,06': setorA1426,
               '01,04,02,06,03': setorA14263, 
               '01,04,02,06,03,25,26': setorA142632526,
               '01,04,06': setorA146, '21,22,27': setorA212227,
               '03': setorA3, np.nan:''}
   setorA = my_dict.get(row[8])
   if pd.isnull(setorA):
      setorA = ''
   else:
      setorA = my_dict.get(row[8])

   user = USER.format(**locals())
   output.write(user)
output.write("</entity-data>")
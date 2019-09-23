import pandas as pd
import math
import numpy as np
from montagem import *
from roles import *

USER  = User()

MI  = MIandME.MI()
ME  = MIandME.ME()
SalesHierarchy  = sales()

setorA3  = setor.a3()
setorA27  = setor.a27()
setorA21  = setor.a21()
setorA2122  = setor.a21() + setor.a22()
setorA142  = setor.a142()
setorA1426  = setor.a142() + setor.a6()
setorA14263  = setorA1426 + setor.a3()
setorA2526  = setor.a2526()
setorA146  = setor.a146()
setorA212227 = setorA2122 + setorA27
setorA142632526  = setorA14263 + setorA2526

dados = pd.read_csv('data/USERS.csv', sep=';')
output = open('data/user.xml ', 'w')

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
   elif (businessPosition == 'MarketingStrategy' and businessArea == 'Marketing' and ('Polymers' in business)):
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
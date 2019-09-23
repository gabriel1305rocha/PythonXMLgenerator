import pandas as pd
import numpy as np
from roles import *
def User():
    USERxml = """
    <VUser>
        <VName>{user}</VName>
        <VPassword>{password}</VPassword>
        <VFullName>{fullname}</VFullName>
        <VEmail>{email}</VEmail>
        <VValidity>01/01/2001..eot</VValidity>
        <VDefaultUOM>TO</VDefaultUOM>
        <VDefaultCurrency>BRL</VDefaultCurrency>
        <EmployeeID>{employeeid}</EmployeeID>
        <VReportsTo>{reportTo}</VReportsTo>
        <Business>{business}</Business>
        <BusinessArea>{businessArea}</BusinessArea>
        <BusinessPosition>{businessPosition}</BusinessPosition>
        <VGroups> 
            {groups}{SalesHierarchy}
            {setorA}
        </VGroups>
        <VRoles>{roleOK}
        </VRoles>
        <VIsSysAdmin>false</VIsSysAdmin>
        <VDefaultLocale>pt_BR</VDefaultLocale>
    </VUser>"""
    return USERxml
class MIandME():
    def MI():
        MIxml = """<VGroup>GeographyHierarchy-GeographyLevel3-Brazil~GeographyHierarchyGroup</VGroup>"""
        return MIxml
    def ME():
        MExml = """<VGroup>GeographyHierarchy-GeographyLevel3-AE~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-AR~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-AT~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-AU~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-BD~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-BE~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-BG~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-BO~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-BS~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CA~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CH~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CL~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CN~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CO~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CR~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-CZ~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-DE~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-DK~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-DO~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-EC~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-EG~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-ES~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-FR~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-GB~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-GT~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-HK~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-HR~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-ID~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-IL~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-IN~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-IT~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-JO~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-JP~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-KR~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-LB~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-LT~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-LU~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-MA~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-MU~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-MX~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-MY~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-NL~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-NZ~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-PA~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-PE~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-PL~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-PT~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-PY~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-RU~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-SA~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-SE~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-SG~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-SI~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-SK~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-SV~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-TR~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-TW~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-US~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-UY~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-VE~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-VG~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-VN~GeographyHierarchyGroup</VGroup>
                <VGroup>GeographyHierarchy-GeographyLevel3-ZA~GeographyHierarchyGroup</VGroup>"""
        return MExml

def sales():
    SalesHierarchyxml = """
            <VGroup>SalesHierarchy-SalesLevel1-BR10~SalesHierarchyGroup</VGroup>
            <VGroup>SalesHierarchy-SalesLevel2-BR10~SalesHierarchyGroup</VGroup>
            <VGroup>SalesHierarchy-VSalesOrg-BR10~SalesHierarchyGroup</VGroup>"""
    return SalesHierarchyxml

class setor():
    def a21():
        setorA21xml = """<VGroup>SABR100121~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA21xml

    def a22():
        setorA22xml = """\n            <VGroup>SABR100122~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA22xml
        
    def a27():
        setorA27xml = """<VGroup>SABR100127~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA27xml

    def a142():
        setorA142xml = """<VGroup>SABR100101~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>
            <VGroup>SABR100104~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>
            <VGroup>SABR100102~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA142xml

    def a6():
        setorA6xml = """\n            <VGroup>SABR100106~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA6xml

    def a3():
        setorA3xml ="""\n            <VGroup>SABR100103~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA3xml

    def a2526():
        setorA2526xml = """<VGroup>SABR100125~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>
            <VGroup>SABR100126~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA2526xml

    def a146():
        setorA146xml = """<VGroup>SABR100101~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>
            <VGroup>SABR100104~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>
            <VGroup>SABR100106~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA146xml
    
    def a3():
        setorA3xml = """<VGroup>SABR100103~com.vendavo.entitlement.api.VSalesAreaGroup</VGroup>"""
        return setorA3xml
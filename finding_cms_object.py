import json
# def zsqlanddtml(self):
    # cms = getattr(self, 'cms')
    # return cms.objectItems()
import pdb;pdb.set_trace()
    # list1 = cms.objectItems()
    # print(list1)
# with open('cms_object_items.json', 'r') as k:
#     list1 = json.load(k)
list1 = [('error_log', <SiteErrorLog at /cms/error_log>), ('ZeReinstallComponent', <ExternalMethod at /cms/ZeReinstallComponent>), ('MaildropHost', <Products.MaildropHost.MaildropHost.MaildropHost object at 0x7f4052c3bbd0 oid 0x4c795 in <Connection at 7f405c68ce90>>), ('ICM_Database_Connection', <SAWrapper at /cms/ICM_Database_Connection>), ('portal_login', <DirectoryViewSurrogate at /cms/portal_login>), ('ICM_MIRROR_Database_Connection', <SAWrapper at /cms/ICM_MIRROR_Database_Connection>), ('acl_users', <exUserFolder at /cms/acl_users>), ('CE_exports', <Folder at /cms/CE_exports>), ('POC_exports', <Folder at /cms/POC_exports>), ('Topic_Views', <Folder at /cms/Topic_Views>), ('enclosures', <Folder at /cms/enclosures>), ('sentinelUploads', <Folder at /cms/sentinelUploads>), ('WorkList_exports', <Folder at /cms/WorkList_exports>), ('signature_logos', <LocalFS at /cms/signature_logos>), ('notice_logos', <LocalFS at /cms/notice_logos>), ('faxes', <LocalFS at /cms/faxes>), ('custom_reports', <LocalFS at /cms/custom_reports>), ('odg', <LocalFS at /cms/odg>), ('zelog', <FileLogger at /cms/zelog>), ('encounter_idn_cache', <RAMCacheManager at /cms/encounter_idn_cache>), ('grp_letter_cache', <RAMCacheManager at /cms/grp_letter_cache>), ('patient_info_cache', <RAMCacheManager at /cms/patient_info_cache>), ('precert_group_cache', <RAMCacheManager at /cms/precert_group_cache>), ('usethishttpcachefor_imagesand_otherblobs', <AcceleratedHTTPCacheManager at /cms/usethishttpcachefor_imagesand_otherblobs>), ('usethishttpcachefor_dashboard', <AcceleratedHTTPCacheManager at /cms/usethishttpcachefor_dashboard>), ('usethishttpcachefor_xml', <AcceleratedHTTPCacheManager at /cms/usethishttpcachefor_xml>), ('logout', <DTMLDocument at /cms/logout>), ('disclaimer', <DTMLDocument at /cms/disclaimer>), ('TermsCond', <DTMLDocument at /cms/TermsCond>), ('contact', <DTMLDocument at /cms/contact>), ('EULA', <DTMLDocument at /cms/EULA>), ('reportimages', <Products.BTreeFolder2.BTreeFolder2.BTreeFolder2 object at 0x7f4052c78f50 oid 0x4c79d in <Connection at 7f405c68ce90>>), ('signatureimages', <Products.BTreeFolder2.BTreeFolder2.BTreeFolder2 object at 0x7f4052c9a150 oid 0x4c7a8 in <Connection at 7f405c68ce90>>), ('utils', <Folder at /cms/utils>), ('tinymce', <TinyMCE at /cms/>), ('Search_Error_Exports', <Folder at /cms/Search_Error_Exports>), ('JivaMember', ), ('JivaProvider', ), ('ZeUtil', <ZeUtil at /cms/ZeUtil>), ('ZeSession', <ZeSession at /cms/ZeSession>), ('Widget', <ZeWidget at /cms/Widget>), ('ZeCache', <ZeCache at /cms/ZeCache>), ('ZeSMS', <ZeSMS at /cms/ZeSMS>), ('ZeSecurity', <ZeSecurity at /cms/ZeSecurity>), ('ZeUI', <ZeUI at /cms/ZeUI>), ('main', <Folder at /cms/main>), ('standard_error_message', <DTMLMethod at /cms/standard_error_message>), ('user_report', <DTMLMethod at /cms/user_report>), ('Sentinel', <Folder at /cms/Sentinel>), ('EDI', <Folder at /cms/EDI>), ('IPEpisode', <ZeJiva at /cms/IPEpisode>), ('OPEpisode', <ZeJiva at /cms/OPEpisode>), ('SAEpisode', <ZeJiva at /cms/SAEpisode>), ('AppealEpisode', <ZeJiva at /cms/AppealEpisode>), ('ReConsiderationEpisode', <ZeJiva at /cms/ReConsiderationEpisode>), ('IssuesEpisode', <ZeJiva at /cms/IssuesEpisode>), ('InquiryEpisode', <ZeJiva at /cms/InquiryEpisode>), ('CMEpisode', <ZeJiva at /cms/CMEpisode>), ('CoachEpisode', <ZeJiva at /cms/CoachEpisode>), ('MMEpisode', <ZeJiva at /cms/MMEpisode>), ('PDEpisode', <ZeJiva at /cms/PDEpisode>), ('PREpisode', <ZeJiva at /cms/PREpisode>), ('QREpisode', <ZeJiva at /cms/QREpisode>), ('WCCMEpisode', <ZeJiva at /cms/WCCMEpisode>), ('WCFCMEpisode', <ZeJiva at /cms/WCFCMEpisode>), ('BHEpisode', <ZeJiva at /cms/BHEpisode>), ('DMEpisode', <ZeJiva at /cms/DMEpisode>), ('OPREpisode', <ZeJiva at /cms/OPREpisode>), ('LCNEpisode', <ZeJiva at /cms/LCNEpisode>), ('TransplantEpisode', <ZeJiva at /cms/TransplantEpisode>), ('PECEpisode', <ZeJiva at /cms/PECEpisode>), ('MCREpisode', <ZeJiva at /cms/MCREpisode>), ('MRIPEpisode', <ZeJiva at /cms/MRIPEpisode>), ('PNEpisode', <ZeJiva at /cms/PNEpisode>), ('ALJEpisode', <ZeJiva at /cms/ALJEpisode>), ('DSHSEpisode', <ZeJiva at /cms/DSHSEpisode>), ('IROEpisode', <ZeJiva at /cms/IROEpisode>), ('CallEpisode', <ZeJiva at /cms/CallEpisode>), ('COCEpisode', <ZeJiva at /cms/COCEpisode>), ('HPEpisode', <ZeJiva at /cms/HPEpisode>), ('BHIPEpisode', <ZeJiva at /cms/BHIPEpisode>), ('BHOPEpisode', <ZeJiva at /cms/BHOPEpisode>), ('BHCMEpisode', <ZeJiva at /cms/BHCMEpisode>), ('MTMEpisode', <ZeJiva at /cms/MTMEpisode>), ('PEEpisode', <ZeJiva at /cms/PEEpisode>), ('Episode', <ZeJiva at /cms/Episode>), ('Address', <ZeJiva at /cms/Address>), ('Attorney', <ZeJiva at /cms/Attorney>), ('Adjuster', <ZeJiva at /cms/Adjuster>), ('Lookup', <ZeJiva at /cms/Lookup>), ('Alerts', <ZeJiva at /cms/Alerts>), ('Billing', <ZeJiva at /cms/Billing>), ('Contact', <ZeJiva at /cms/Contact>), ('Calendar', <ZeJiva at /cms/Calendar>), ('CostSavings', <ZeJiva at /cms/CostSavings>), ('Document', <ZeJiva at /cms/Document>), ('Message', <ZeJiva at /cms/Message>), ('Diagnosis', <ZeJiva at /cms/Diagnosis>), ('Issues', <ZeJiva at /cms/Issues>), ('Reports', <ZeJiva at /cms/Reports>), ('Extensions', <ZeJiva at /cms/Extensions>), ('Assessment', <ZeJiva at /cms/Assessment>), ('PlanOfCare', <ZeJiva at /cms/PlanOfCare>), ('Claim', <ZeJiva at /cms/Claim>), ('Notification', <ZeJiva at /cms/Notification>), ('NewsLetter', <ZeJiva at /cms/NewsLetter>), ('Guidelines', <ZeJiva at /cms/Guidelines>), ('AuditTrack', <ZeJiva at /cms/AuditTrack>), ('EducationalMaterial', <ZeJiva at /cms/EducationalMaterial>), ('ZeUser', <ZeJiva at /cms/ZeUser>), ('Payor', <ZeJiva at /cms/Payor>), ('Procedure', <ZeJiva at /cms/Procedure>), ('Activity', <ZeJiva at /cms/Activity>), ('Notes', <ZeJiva at /cms/Notes>), ('Patient', <ZeJiva at /cms/Patient>), ('UDF', <ZeJiva at /cms/UDF>), ('Incentive', <ZeJiva at /cms/Incentive>), ('Enrollment', <ZeJiva at /cms/Enrollment>), ('OutReachScript', <ZeJiva at /cms/OutReachScript>), ('WorkFlow', <ZeJiva at /cms/WorkFlow>), ('Provider', <ZeJiva at /cms/Provider>), ('Fax', <ZeJiva at /cms/Fax>), ('AutoComplete', <ZeJiva at /cms/AutoComplete>), ('Email', <ZeJiva at /cms/Email>), ('ProviderPortal', <ZeJiva at /cms/ProviderPortal>), ('UMService', <ZeJiva at /cms/UMService>), ('Keyword', <ZeJiva at /cms/Keyword>), ('MemberPortal', <ZeJiva at /cms/MemberPortal>), ('ZeOffline', <ZeJiva at /cms/ZeOffline>), ('ActivityWorkFlow', <ZeJiva at /cms/ActivityWorkFlow>), ('BHService', <ZeJiva at /cms/BHService>), ('CallTracking', <ZeJiva at /cms/CallTracking>), ('WorkList', <ZeJiva at /cms/WorkList>), ('Emmi', <ZeJiva at /cms/Emmi>), ('Healthwise', <ZeJiva at /cms/Healthwise>), ('Medispan', <ZeJiva at /cms/Medispan>), ('PHMRegistry', <ZeJiva at /cms/PHMRegistry>), ('IPCensus', <ZeJiva at /cms/IPCensus>), ('Aco', <ZeJiva at /cms/Aco>), ('Dashboard', <ZeJiva at /cms/Dashboard>), ('CPMDashboard', <ZeJiva at /cms/CPMDashboard>), ('SQDashboard', <ZeJiva at /cms/SQDashboard>), ('LTSSEpisode', <ZeJiva at /cms/LTSSEpisode>), ('CareReminder', <ZeJiva at /cms/CareReminder>), ('MAAppealEpisode', <ZeJiva at /cms/MAAppealEpisode>), ('MAGrievanceEpisode', <ZeJiva at /cms/MAGrievanceEpisode>), ('Review', <ZeJiva at /cms/Review>), ('Medications', <ZeJiva at /cms/Medications>), ('ExtCalendar', <ZeJiva at /cms/ExtCalendar>), ('InterfaceLog', <InterfaceLog at /cms/InterfaceLog>), ('SQLWrapper', <ZeMSSQLWrapper at SQLWrapper>), ('Permission', <MASSPermissionCtrl at /cms/Permission>), ('mbr_portal', <DTMLMethod at /cms/mbr_portal>), ('prv_portal', <DTMLMethod at /cms/prv_portal>)]
ze = []
dtml1 = []
folder = []
sawrapper = []
products = []
tinymce = []
acceratedhttp = []
ramcachemanager = []
externalmethod = []
siteerrorlog = []
localfs = []
filelogger = []
exuserfolder = []
interfacelog = []
masspermission = []
directoryviewsurrogate = []
dtmlmethod1 = []
all = []
no_type = []
for tup in list1:
    t = str(tup[1]).split(" ")
    if t[0].startswith("<Ze"):
        # print(type(t[0]))
        ze.append(tup[0])
    elif t[0].startswith("<Folder"):
        folder.append(tup[0])
    elif t[0].startswith("<DTMLDocument"):
        import pdb;pdb.set_trace()
        dtml1.append(tup[0])
    elif t[0].startswith("<SAWrapper"):
        sawrapper.append(tup[0])
    elif t[0].startswith("<Products"):
        products.append(tup[0])
    elif t[0].startswith("<TinyMCE"):
        tinymce.append(tup[0])
    elif t[0].startswith("<AcceleratedHTTPCacheManager"):
        acceratedhttp.append(tup[0])
    elif t[0].startswith("<RAMCacheManager"):
        ramcachemanager.append(tup[0])
    elif t[0].startswith("<ExternalMethod"):
        externalmethod.append(tup[0])
    elif t[0].startswith("<SiteErrorLog"):
        siteerrorlog.append(tup[0])
    elif t[0].startswith("<LocalFS"):
        localfs.append(tup[0])
    elif t[0].startswith("<FileLogger"):
        filelogger.append(tup[0])
    elif t[0].startswith("<exUserFolder"):
        exuserfolder.append(tup[0])
    elif t[0].startswith("<InterfaceLog"):
        interfacelog.append(tup[0])
    elif t[0].startswith("<MASSPermissionCtrl"):
        masspermission.append(tup[0])
    elif t[0].startswith("<DirectoryViewSurrogate"):
        directoryviewsurrogate.append(tup[0])
    elif t[0].startswith("<DTMLMethod"):
        import pdb;pdb.set_trace()
        dtmlmethod1.append(tup[0])
    # elif t[0].startswith(""):
    #     no_type.append(tup[0])
    else:
        all.append(tup)
    # print(type(tup[1]))
print(ze)
print(folder)
print(dtmlmethod1)
print(dtml1)
print(sawrapper)
print(products)
print(tinymce)
print(acceratedhttp)
print(ramcachemanager)
print(externalmethod)
print(siteerrorlog)
print(localfs)
print(filelogger)
print(exuserfolder)
print(interfacelog)
print(masspermission)
print(directoryviewsurrogate)
# print(no_type)
# print(all)
# for t in ll:
#     line = ''.join(str(x) for x in t)
#     file1.write(line + '\n')
# file1.write(("").join(str(ll)))
# file1.close()
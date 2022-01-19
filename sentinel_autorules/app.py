
import json
from os import path
from pathlib import Path
from tkinter import *
from tkinter import ttk
from functools import partial
from datetime import datetime

#declaring GUI elements
main = Tk()
main.title("Choose your Data Connectors")
main.geometry("+250+250")
frame = ttk.Frame(main, padding=(3, 3, 0, 12))
frame.grid(column=0, row=0, sticky=(N, S, E, W))
scrollbar = Scrollbar(main)

#declaring GUI variables
values = StringVar()
values.set("AzureActiveDirectory AzureActiveDirectory-IdentityProtection AWS AWSS3 AzureKeyVault Apache AzureMonitorIIS AzureFirewall Box CiscoUmbrella CiscoISE DefenderForCloudApps DefenderForEndpoint DefenderForIdentity DefenderForOffice365 GCP Office365 Proofpoint Syslog SecurityEvents SAP")
lstbox = Listbox(frame, listvariable=values, selectmode=MULTIPLE, width=37, height=15)
lstbox.grid(column=0, row=0, columnspan=2)

#declaring Schema
Schema = Path(__file__).parent / 'schema_template.json'
reslist = list()
#declaring data connector variables
AAD = Path(__file__).parent / 'DC/Azure Active Directory.json'
AADIdentityProtection = Path(__file__).parent / 'DC/AAD Identity Protection.json'
AWS = Path(__file__).parent / 'DC/AWS.json'
AWSS3 = Path(__file__).parent / 'DC/AWS_S3.json'
AKS = Path(__file__).parent / 'DC/Azure Key Vault.json'
Apache = Path(__file__).parent / 'DC/Apache.json'
AzureMonitorIIS = Path(__file__).parent / 'DC/Azure Monitor (IIS).json'
AzureFirewall = Path(__file__).parent / 'DC/Azure Firewall.json'
Box = Path(__file__).parent / 'DC/Box.json'
CiscoUmbrella = Path(__file__).parent / 'DC/Cisco Umbrella.json'
CiscoISE = Path(__file__).parent / 'DC/CiscoISE.json'
DefenderForCloudApps = Path(__file__).parent / 'DC/Defender for Cloud Apps.json'
DefenderForEndpoint = Path(__file__).parent / 'DC/Defender for Endpoint.json'
DefenderForIdentity = Path(__file__).parent / 'DC/Defender for Identity.json'
DefenderForOffice365 = Path(__file__).parent / 'DC/Defender for Office365.json'
GCPIAM = Path(__file__).parent / 'DC/GCP IAM.json'
Office365 = Path(__file__).parent / 'DC/Office365.json'
Proofpoint = Path(__file__).parent / 'DC/Proofpoint.json'
Syslog = Path(__file__).parent / 'DC/Syslog.json'
SecurityEvents = Path(__file__).parent / 'DC/Security Events.json'
SAP = Path(__file__).parent / 'DC/SAP.json'



#opening files with JSON data
schemafile = open(Schema)
AADfile = open(AAD)
AADIPfile = open(AADIdentityProtection)
AWSfile = open(AWS)
AWSS3file = open (AWSS3)
AzureMonitorIISfile = open(AzureMonitorIIS)
apachefile = open(Apache)
AKSfile = open(AKS)
AzureFirewallfile = open(AzureFirewall)
Boxfile = open(Box)
CiscoUmbrellafile = open(CiscoUmbrella)
CiscoISEfile = open(CiscoISE)
DefenderForCloudAppsfile = open(DefenderForCloudApps)
DefenderForEndpointfile = open(DefenderForEndpoint)
DefenderForIdentityfile = open(DefenderForIdentity)
DefenderForOfficefile = open(DefenderForOffice365)
GCPIAMfile = open(GCPIAM)
Office365file = open(Office365)
Proofpointfile = open(Proofpoint)
SAPfile = open(SAP)
syslogfile = open(Syslog)
sefile = open(SecurityEvents)


#loading those files as JSON
SchemaTemplate = json.load(schemafile)
AADdata = json.load(AADfile)
AADIPdata = json.load(AADIPfile)
AWSdata = json.load(AWSfile)
AWSS3data = json.load(AWSS3file)
AzureMonitorIISdata = json.load(AzureMonitorIISfile)
Apachedata = json.load(apachefile)
AKSdata = json.load(AKSfile)
AzureFWdata = json.load(AzureFirewallfile)
Boxdata = json.load(Boxfile)
CiscoUmbrelladata = json.load(CiscoUmbrellafile)
CiscoISEdata = json.load(CiscoISEfile)
MCASdata = json.load(DefenderForCloudAppsfile)
MDEdata = json.load(DefenderForEndpointfile)
MDIdata = json.load(DefenderForIdentityfile)
MDOdata = json.load(DefenderForOfficefile)
GCPdata = json.load(GCPIAMfile)
Office365data = json.load(Office365file)
Proofpointdata = json.load(Proofpointfile)
SAPdata = json.load(SAPfile)
Syslogdata = json.load(syslogfile)
SEdata = json.load(sefile)
#creating empty lists to hold parsed JSON 
requestedRuleset = SchemaTemplate['resources']


def create_rules(ruleset):
    if 'Syslog' in ruleset:
        print('Adding Syslog data to the ruleset')
        for x in Syslogdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'AzureActiveDirectory' in ruleset:
        print('Adding Azure Active Directory use-cases to the ruleset')
        for x in AADdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'SecurityEvents' in ruleset:
        print('Adding Security Events use-cases to the ruleset')
        for x in SEdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'AzureActiveDirectory-IdentityProtection' in ruleset:
        print('Adding Azure Active Directory - Identity Protection use-cases to the ruleset')
        for x in AADIPdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'AWS' in ruleset:
        print('Adding AWS use-cases to the ruleset')
        for x in AWSdata['resources']: 
            SchemaTemplate['resources'].append(x)
    if 'AWSS3' in ruleset:
        print('Adding AWSS3 use-cases to the ruleset')
        for x in AWSS3data['resources']:
            SchemaTemplate['resources'].append(x)
    if 'AzureMonitorIIS' in ruleset:
        print('Adding AzureMonitorIIS use-cases to the ruleset')
        for x in AzureMonitorIISdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'AzureKeyVault' in ruleset:
        print('Adding AzureKeyVault use-cases to the ruleset')
        for x in AKSdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'AzureFirewall' in ruleset:
        print('Adding Azure Firewall use-cases to the ruleset')
        for x in AzureFWdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'Apache' in ruleset:
        print('Adding Apache use-cases to the ruleset')
        for x in Apachedata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'Box' in ruleset:
        print('Adding Box use-cases to the ruleset')
        for x in Boxdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'CiscoUmbrella' in ruleset:
        print('Adding Cisco Umbrella use-cases to the ruleset')
        for x in CiscoUmbrelladata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'CiscoISE' in ruleset:
        print('Adding CiscoISE use-cases to the ruleset')
        for x in CiscoISEdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'DefenderForCloudApps' in ruleset:
        print('Adding Defender for Cloud Apps use-cases to the ruleset')
        for x in MCASdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'DefenderForEndpoint' in ruleset:
        print('Adding Defender for Endpoint use-cases to the ruleset')
        for x in MDEdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'DefenderForIdentity' in ruleset:
        print('Adding Defender for Identity use-cases to the ruleset')
        for x in MDIdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'DefenderForOffice365' in ruleset:
        print('Adding Defender for Office365 use-cases to the ruleset')
        for x in MDOdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'GCP' in ruleset:
        print('Adding GCP IAM use-cases to the ruleset')
        for x in GCPdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'Proofpoint' in ruleset:
        print('Adding Proofpoint use-cases to the ruleset')
        for x in Proofpointdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'SAP' in ruleset:
        print('Adding SAP use-cases to the ruleset')
        for x in SAPdata['resources']:
            SchemaTemplate['resources'].append(x)
    if 'Office365' in ruleset:
        print('Adding Office365 use-cases to the ruleset')
        for x in Office365data['resources']:
            SchemaTemplate['resources'].append(x)    
        SchemaTemplate['resources'].append(x)    

        #appending the existing schema file and dumping it as a unique JSON file
    with open('Azure Sentinel Rules_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.json', 'a') as json_file:
        json.dump(SchemaTemplate, json_file)

def close_GUI():
    main.destroy()

def show_GUI():
    reslist = list()
    selection = lstbox.curselection()   
    for i in selection:
        entry = lstbox.get(i)
        reslist.append(entry)
    for val in reslist:         
        print(reslist)
    create_rules(reslist)
    main.destroy()         
scrollbar.grid(row=0, column=1, sticky=NS)
scrollbar.config(command=lstbox.yview)
btn = ttk.Button(frame, text="Generate", command=show_GUI)
btn.grid(column=0, row=1)
closeBtn = ttk.Button(frame, text="Close", command=close_GUI)
closeBtn.grid(column=1, row=1)
main.mainloop()
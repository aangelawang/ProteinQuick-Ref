
import webbrowser
import pandas as pd
import webbrowser
from flask import Blueprint,render_template,request

searches=Blueprint('searches',__name__)
@searches.route('/home',methods=['GET','POST'])
def home():
    df=pd.read_csv('final2.csv')
    if request.method=='POST':
        prot=request.form.get("protein")
        idx=0
        if df['Gene_Symbol'].isin([prot]).any():
            idx=df[df['Gene_Symbol'].isin([prot])].index[0]
        elif df['Uniprot_Acc'].isin([prot]).any():
            idx=df[df['Uniprot_Acc'].isin([prot])].index[0]
        elif df['Omim ID'].isin([prot]).any():
            idx=df[df['Omim ID'].isin([prot])].index[0]
        elif df['Ensemble Gene ID'].isin([prot]).any():
            idx=df[df['Ensemble Gene ID'].isin([prot])].index[0]
        row=df.loc[idx,:]
        url = 'https://www.proteinatlas.org/' + row[1] + '/subcellular'
        url2='https://www.uniprot.org/uniprot/'+row[1]
        url3 = 'https://depmap.org/portal/gene/' + row[0]
        url4 = 'https://www.cbioportal.org/results/cancerTypesSummary?case_set_id=all&gene_list=' + row[0] + '&cancer_study_list=5c8a7d55e4b046111fee2296'
        url5 = 'https://www.cbioportal.org/results/comparison?case_set_id=all&gene_list=' + row[0] + '&cancer_study_list=5c8a7d55e4b046111fee2296'
        url6 = 'https://www.proteinatlas.org/' + row[1] + '/cell+line'
        url7='https://www.proteinatlas.org/'  + row[1] + '/tissue'
        url8='https://omim.org/entry/'+str(row[2])+'?search='+row[0]+'&highlight='+row[0].lower()+'#geneFunction'
        url9='https://omim.org/entry/'+str(row[2])+'?search='+row[0]+'&highlight='+row[0].lower()+'#animalModel'
        url10 = 'https://pharos.nih.gov/targets/' + row[1]
        url11= 'https://www.mousephenotype.org/data/search?term=' + row[0] +'&type=gene'
        url12 = 'https://platform.opentargets.org/target/' + row[3]
        url13 = 'https://www.uniprot.org/uniprot/' + row[1]+'#subcellular_location'
        if request.form.get('Functions')!=None:
            webbrowser.open(url2)
            webbrowser.open(url8)
        if request.form.get('Animal Models')!=None:
            webbrowser.open(url9)
        if request.form.get('Protein Level in Cell Lines')!=None:
            webbrowser.open(url3)
        if request.form.get('Subcellular Location')!=None:
            webbrowser.open(url)
            webbrowser.open(url13)
        if request.form.get('Tissue Distribution')!=None:
            webbrowser.open(url7)
        if request.form.get('RNA and Protein Expression')!=None:
            webbrowser.open(url6)
        if request.form.get('Mutation Frequency in Cancer and Survival Rate')!=None:
            webbrowser.open(url4)
            webbrowser.open(url5)
        if request.form.get('Mouse Phenotypes')!=None:
            webbrowser.open(url11)
        if request.form.get('Drug Targets')!=None:
            webbrowser.open(url10)
            webbrowser.open(url12)
    return render_template('base.html')

    
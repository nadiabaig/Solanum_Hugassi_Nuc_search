#Solcap SNP array PCoA
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib.patches import Ellipse

from sklearn.preprocessing import StandardScaler
pd.set_option('display.max_columns', None)
cluster_file=pd.read_csv('/1data/Nadia/Project1_SNP_array/copied_geno/Final_analysis_genotyping/fitpoly_SNP_array_potato_analysis/8k_array_concordance/Potato_chips_Full_Data_Table_CGclustered.txt',sep="\t")
spike_cols = [col for col in cluster_file.columns if 'Custom GType' in col] #AABB genos only
cf1=cluster_file[['Name','DE61POTMPZD100048.Custom GType', 'DE88POTMPZD100047.Custom GType', 'DE18POTMPZD100046.Custom GType', 'DE45POTMPZD100045.Custom GType', 'DE72POTMPZD100044.Custom GType', 'DE02POTMPZD100043.Custom GType', 'DE29POTMPZD100042.Custom GType', 'DE56POTMPZD100041.Custom GType', 'DE83POTMPZD100040.Custom GType', 'DE13POTMPZD100039.Custom GType', 'DE40POTMPZD100038.Custom GType', 'DE67POTMPZD100037.Custom GType', 'DE94POTMPZD100036.Custom GType', 'DE24POTMPZD100035.Custom GType', 'DE51POTMPZD100034.Custom GType', 'DE78POTMPZD100033.Custom GType', 'DE08POTMPZD100032.Custom GType', 'DE35POTMPZD100031.Custom GType', 'DE62POTMPZD100030.Custom GType', 'DE89POTMPZD100029.Custom GType', 'DE19POTMPZD100028.Custom GType', 'DE46POTMPZD100027.Custom GType', 'DE73POTMPZD100026.Custom GType', 'DE03POTMPZD100025.Custom GType', 'DE30POTMPZD100024.Custom GType', 'DE57POTMPZD100023.Custom GType', 'DE84POTMPZD100022.Custom GType', 'DE14POTMPZD100021.Custom GType', 'DE41POTMPZD100020.Custom GType', 'DE68POTMPZD100019.Custom GType', 'DE95POTMPZD100018.Custom GType', 'DE25POTMPZD100017.Custom GType', 'DE52POTMPZD100016.Custom GType', 'DE79POTMPZD100015.Custom GType', 'DE09POTMPZD100014.Custom GType', 'DE36POTMPZD100013.Custom GType', 'DE63POTMPZD100012.Custom GType', 'DE90POTMPZD100011.Custom GType', 'DE20POTMPZD100010.Custom GType', 'DE47POTMPZD100009.Custom GType', 'DE74POTMPZD100008.Custom GType', 'DE04POTMPZD100007.Custom GType', 'DE31POTMPZD100006.Custom GType', 'DE58POTMPZD100005.Custom GType', 'DE85POTMPZD100004.Custom GType', 'DE15POTMPZD100003.Custom GType', 'DE42POTMPZD100002.Custom GType', 'DE69POTMPZD100001.Custom GType']].copy()

#renaming cols
cf1.columns=['cust_id_x', 'Panda','Olga','Maxila','Logo','Lady_Rosetta','Kuba','Kolibri','Fitis','Calla','Aspirant','Remarka','Rafaele','Quarta1','Marabel','Lolita','Krone','Gala','Elfe','Carmona','Agila','G87','DG83','P54','P49','p40','P38','P18','P3','Innovator','Impala','Panda','Agria','Berber','Assia','Quarta2','Granola','Adretta','Nicola','Cara','Alcmaria','Saturna','Maris_piper','Desiree','Schwalbe','Aquila','Flava','Hindenburg','Industrie']
#AAAA=0, AAAB=1,AABB=2,ABBB=3, BBBB=4
def alleles_assignment(df):
    # Replace values in 'df' with corresponding replacements
    df = df.replace(['AAAA'], '0')
    df = df.replace(['AAAB'], '1')
    df = df.replace(['AABB'], '2')
    df = df.replace(['ABBB'], '3')
    df = df.replace(['BBBB'], '4')
    #df = df.replace(['NaN'], '-1') #wasn't working
    df = df.fillna('-1')
   
    return df

df_cf1 = alleles_assignment(cf1)
del df_cf1['cust_id_x']

# Perform PCA on the SNP dosage data
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_cf1.values.T)

# Calculate the percentage of variance explained by each PC
explained_variance_ratio = pca.explained_variance_ratio_

# Create a DataFrame for the PCA results
pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])

# Assign diploid and tetraploid labels
pca_df['Genotype'] = ['Diploid' if genotype in diploid_genotypes else 'Tetraploid' for genotype in df_cf1.columns]

# Plot PCA results
fig, ax = plt.subplots(figsize=(10, 8))

# Define colors for diploids and tetraploids
colors = {'Diploid': 'red', 'Tetraploid': 'orange'}

# Plot each genotype separately and label diploid genotypes with names
for genotype, color in colors.items():
    subset = pca_df[pca_df['Genotype'] == genotype]
    ax.scatter(subset['PC1'], subset['PC2'], c=color, label=genotype, alpha=0.8, edgecolors='black', linewidths=0.5)
    if genotype == 'Diploid':
        diploid_subset = subset[subset['Genotype'] == 'Diploid']
        for i in range(len(diploid_subset)):
            genotype_name = df_cf1.columns[df_cf1.columns.isin(diploid_genotypes)][i]
            ax.annotate(genotype_name, (diploid_subset['PC1'].iloc[i], diploid_subset['PC2'].iloc[i]), fontsize=12, ha='center', va='center')

# Add PC1 and PC2 values as axis labels with variance explained
ax.set_xlabel(f'PC1 ({explained_variance_ratio[0]*100:.2f}% of variance)', fontsize=14)
ax.set_ylabel(f'PC2 ({explained_variance_ratio[1]*100:.2f}% of variance)', fontsize=14)

# Calculate the number of groups formed in PCA
kmeans = KMeans(n_clusters=3)  # Update the number of desired clusters
cluster_labels_pca = kmeans.fit_predict(pca_result)
num_groups_pca = len(np.unique(cluster_labels_pca))
print("Number of groups formed in PCA:", num_groups_pca)

# Encircle groups with light-colored ovals
for cluster_id in range(num_groups_pca):
    cluster_points = pca_df[cluster_labels_pca == cluster_id]
    ellipse = Ellipse((np.mean(cluster_points['PC1']), np.mean(cluster_points['PC2'])),
                      width=2 * np.std(cluster_points['PC1']),
                      height=2 * np.std(cluster_points['PC2']),
                      alpha=0.2, facecolor='pink', edgecolor='black')
    ax.add_patch(ellipse)

# Set plot limits and style
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='both', which='both', bottom=False, left=False)

# Show legend
ax.legend()

# Set plot title
plt.title('PCA Analysis 8K array', fontsize=16)

# Display the plot
plt.show()


# Show the plot
plt.savefig('PCOA_8K_array.pdf', format='pdf', dpi=600)
plt.show()


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

labels = ['No','\\textless30','\\textgreater30']

def ttest_acc(acc):
    dif=[]
    acc = np.array(acc)
    for i in range(len(acc)):
        for j in range(i+1,len(acc)):
            dif.append(np.around(acc[i]-acc[j],4))

    dif = np.array(dif)
    for i in range(len(dif)):
        print("Fold-"+str(i+1), end='')
        temp = dif[:,i]
        for j in temp:
            print(" & "+str(j), end=' ')
        print("\\\\ ")

    print("Avg", end='')
    for i in range(len(dif)):
        temp = dif[i,:]
        print(" & "+ str(np.around(temp.mean(),4)), end = '')
    print("\\\\ ")

    print("Std", end='')
    for i in range(len(dif)):
        temp = dif[i,:]
        print(" & "+ str(np.around(temp.std(),4)), end = '')
    print("\\\\ ")

    print("P-Value", end='')
    for i in range(len(acc)):
        for j in range(i+1,len(acc)):
            temp = stats.ttest_rel(acc[i],acc[j])[1]
            print(" & "+str(np.around(temp, 4)), end='')
    print("\\\\ ")

def acc_c(acc) :
    for i in range(len(acc[0])):
        print("Fold-"+str(i+1), end='')
        temp = np.array(acc)[:,i]
        for j in temp:
            print(" & "+str(np.around(j, 4)), end='')
        print("\\\\ ")
    print(" ")
    
    print("Avg", end='')
    for i in range(len(acc)):
        temp = np.array(acc)[i,:]
        print(" & "+str(np.around(temp.mean(),4)), end = '')
    print("\\\\ ")

    print("Std", end='')
    for i in range(len(acc)):
        temp = np.array(acc)[i,:]
        print(" & "+str(np.around(temp.std(), 4)), end='')
    print("\\\\ ")

mask_percentage = [0, 0.1, 0.2, 0.5, 0.9, 0.95]

def acc_c2(acc) :
    for i in range(len(acc[0])):
        print(str(mask_percentage[i]), end='')
        temp = np.array(acc)[:,i]
        for j in temp:
            print(" & "+str(np.around(j, 4)), end='')
        print("\\\\ ")
    print(" ")
    
    print("Avg", end='')
    for i in range(len(acc)):
        temp = np.array(acc)[i,:]
        print(" & "+str(np.around(temp.mean(),4)), end = '')
    print("\\\\ ")

    print("Std", end='')
    for i in range(len(acc)):
        temp = np.array(acc)[i,:]
        print(" & "+str(np.around(temp.std(), 4)), end='')
    print("\\\\ ")

def ttest_acc2(acc):
    dif=[]
    acc = np.array(acc)
    for i in range(len(acc)):
        for j in range(i+1,len(acc)):
            dif.append(np.around(acc[i]-acc[j],4))

    dif = np.array(dif)
    for i in range(len(dif[0])):
        print(str(mask_percentage[i]), end='')
        temp = dif[:,i]
        for j in temp:
            print(" & "+str(j), end=' ')
        print("\\\\ ")

    print("Avg", end='')
    for i in range(len(dif)):
        temp = dif[i,:]
        print(" & "+ str(np.around(temp.mean(),4)), end = '')
    print("\\\\ ")

    print("Std", end='')
    for i in range(len(dif)):
        temp = dif[i,:]
        print(" & "+ str(np.around(temp.std(),4)), end = '')
    print("\\\\ ")

    print("P-Value", end='')
    for i in range(len(acc)):
        for j in range(i+1,len(acc)):
            temp = stats.ttest_rel(acc[i],acc[j])[1]
            print(" & "+str(np.around(temp, 4)), end='')
    print("\\\\ ")

def other2(other):
    for i in range(len(other[0])):
        temp = np.array(other)[:,i]
        for j in range(temp.shape[1]):
            it = temp[:,j]
            for idx, k in enumerate(it):
                if idx==0 and j == 1:
                    print(str(mask_percentage[i])+" & "+ labels[j]+" & "+str(np.around(k, 4)), end='')
                elif idx==0:
                    print(" & "+ labels[j]+" & "+str(np.around(k, 4)), end='')
                else:
                    print(" & "+str(np.around(k, 4)), end='')
            print("\\\\ ")
    print(" ")
    mean = np.average(other,axis =1)
    for i in range(mean.shape[1]):
        it = mean[:,i]
        for idx, k in enumerate(it):
            if idx==0 and i == 1:
                print("Avg & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            elif idx==0:
                print(" & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            else:
                print(" & "+str(np.around(k, 4)), end='')
        print("\\\\ ")

    std = np.std(other,axis =1)
    for i in range(std.shape[1]):
        it = std[:,i]
        for idx, k in enumerate(it):
            if idx==0 and i == 1:
                print("Std & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            elif idx==0:
                print(" & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            else:
                print(" & "+str(np.around(k, 4)), end='')
        print("\\\\ ")

def other(other):
    for i in range(len(other[0])):
        temp = np.array(other)[:,i]
        for j in range(temp.shape[1]):
            it = temp[:,j]
            for idx, k in enumerate(it):
                if idx==0 and j == 1:
                    print("Fold-"+str(i+1)+" & "+ labels[j]+" & "+str(np.around(k, 4)), end='')
                elif idx==0:
                    print(" & "+ labels[j]+" & "+str(np.around(k, 4)), end='')
                else:
                    print(" & "+str(np.around(k, 4)), end='')
            print("\\\\ ")
    print(" ")
    mean = np.average(other,axis =1)
    for i in range(mean.shape[1]):
        it = mean[:,i]
        for idx, k in enumerate(it):
            if idx==0 and i == 1:
                print("Avg & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            elif idx==0:
                print(" & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            else:
                print(" & "+str(np.around(k, 4)), end='')
        print("\\\\ ")

    std = np.std(other,axis =1)
    for i in range(std.shape[1]):
        it = std[:,i]
        for idx, k in enumerate(it):
            if idx==0 and i == 1:
                print("Std & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            elif idx==0:
                print(" & "+ labels[i]+" & "+str(np.around(k, 4)), end='')
            else:
                print(" & "+str(np.around(k, 4)), end='')
        print("\\\\ ")

print("------------recall-----------")
recall_rf=[[0.5833695180199739, 0.5273556231003039, 0.6539296569691706], [0.5334346504559271, 0.48349978289188017, 0.662613981762918], [0.5234476769431177, 0.4769865392965697, 0.617455492835432], [0.7709509335649153, 0.49848024316109424, 0.597047329570126], [0.9806773773339122, 0.49978289188015634, 0.6538545059717699], [0.9763352149370387, 0.5180199739470256, 0.6304017372421281], [0.9821971341728181, 0.4905537459283388, 0.6287451150673035], [0.9780720798957881, 0.4970684039087948, 0.6506730351715154], [0.9845819761129208, 0.5629613547546678, 0.6042118975249674], [0.9897937024972856, 0.5349544072948328, 0.5529743812418585]]
recall_svm=[[0.3981762917933131, 0.3840642640034737, 0.7429439861050803], [0.3892748588797221, 0.37755102040816324, 0.7570560138949197], [0.3658271819366044, 0.3747286148501954, 0.6656534954407295], [0.6745549283543204, 0.41033434650455924, 0.654363873208858], [0.9164133738601824, 0.3962223187147199, 0.7148751357220413], [0.9170646982197134, 0.42813721233174123, 0.6851248642779587], [0.9142422926617455, 0.38914223669924, 0.6732522796352584], [0.9125054277029961, 0.41454940282301844, 0.7075553625705602], [0.9129207383279044, 0.35692574902301344, 0.6320017368649588], [0.9114006514657981, 0.1471993052540165, 0.5979157620495007]]
recall_dt=[[0.4331306990881459, 0.4429005644811116, 0.5419018671298307], [0.35953104646113765, 0.4259661311333044, 0.5379939209726444], [0.36539296569691704, 0.4107685627442466, 0.4963091619626574], [0.6191923577941815, 0.424880590534086, 0.4889274858879722], [0.8371689101172384, 0.4266174554928354, 0.5281216069489685], [0.8467216673903604, 0.4368215371254885, 0.5233441910966341], [0.8447676943117672, 0.4023887079261672, 0.5338688666956144], [0.8302214502822406, 0.4262757871878393, 0.5245332175423361], [0.8484256243213898, 0.4537559704732957, 0.5065132435953105], [0.9029315960912052, 0.37646547980894485, 0.490447242726878]]
recall_nb=[[0.6487190620929223, 0.20017368649587494, 0.5440729483282675], [0.6613113330438558, 0.18910117238384716, 0.5683890577507599], [0.7069040382110291, 0.2029960920538428, 0.5015197568389058], [0.7954841511072515, 0.22253582283977422, 0.43356491532783326], [0.8232739904472427, 0.16934433347807207, 0.5094462540716612], [0.822405557967868, 0.17954841511072514, 0.48512486427795876], [0.8167607468519322, 0.13832790445168294, 0.49413808076422056], [0.8048198002605298, 0.16786102062975028, 0.49804602692140687], [0.8123778501628665, 0.1556665219279201, 0.4730785931393834], [0.8221498371335505, 0.07490230134607034, 0.5017368649587495]]
recall_knn = [[0.8931828050369084, 0.42249240121580545, 0.48219713417281806], [0.8647416413373861, 0.40316977854971775, 0.4969604863221885], [0.868866695614416, 0.37407729049066435, 0.4418150238818932], [0.9148936170212766, 0.402301346070343, 0.45310464611376466], [0.9780720798957881, 0.4194528875379939, 0.48555917480998917], [0.9743812418584455, 0.4363873208858011, 0.49077090119435396], [0.9761181068171949, 0.4102062975027144, 0.4865392965696917], [0.9752496743378203, 0.4264929424538545, 0.5156317846287451], [0.9767643865363735, 0.5505861919235779, 0.47850629613547546], [0.9802388707926167, 0.8280503690838037, 0.4683022145028224]]
recall = []
recall.append(recall_rf)
recall.append(recall_svm)
recall.append(recall_dt)
recall.append(recall_nb)
recall.append(recall_knn)
# other(recall)

print("------------nrecall-----------")
nrecall_rf=[[0.9256404689535389, 0.7364307425097699, 0.7202561875814155], [0.9129396439426835, 0.7224272687798524, 0.7044072948328267], [0.8429222752930959, 0.7181936604429006, 0.7478289188015632], [0.892748588797221, 0.7647633521493704, 0.7757273122014763], [0.9095646509608077, 0.8470307241341873, 0.8105731654363874], [0.9065248072956248, 0.8375854956030833, 0.818280503690838], [0.9039192270111823, 0.8416196265740339, 0.8052328737379221], [0.9075018999022907, 0.8533434650455927, 0.802084464227554], [0.8663699522362136, 0.8318315058082727, 0.8776462924763869], [0.7608554059921842, 0.7993703180979264, 0.9786125284985343]]
nrecall_svm=[[0.915327833260964, 0.7572731220147634, 0.5899913156752062], [0.9169561441597915, 0.7324142422926617, 0.6125705601389492], [0.8152409900130265, 0.6989795918367347, 0.6888840642640035], [0.8729917498914459, 0.7734476769431177, 0.7231871471993052], [0.8754749755726848, 0.8713494734556508, 0.7669344333478072], [0.8835088481163826, 0.852893279774183, 0.7787668258792879], [0.8730865269786126, 0.8530178028658272, 0.7622407990446206], [0.8739550537400934, 0.8698436821537125, 0.7735316469438714], [0.7751845419018671, 0.8303115839756813, 0.8454022364564108], [0.5982414242292662, 0.7962219085875584, 0.9337748344370861]]
nrecall_dt=[[0.6047546678245767, 0.8747286148501954, 0.7169995657837603], [0.6226660877116804, 0.8689752496743378, 0.7177594442032132], [0.5614415979157621, 0.8818931828050369, 0.7623751628310899], [0.5237733391228832, 0.8854754667824577, 0.8165436387320886], [0.534795353381826, 0.9208554988600586, 0.7953755970473295], [0.5244815980892411, 0.9213983280859841, 0.7976552323056882], [0.5242644663988709, 0.9199956578376032, 0.780371295190533], [0.5173162523070242, 0.9284628745115068, 0.789599392031267], [0.5055362570560139, 0.914992943220063, 0.800021713169037], [0.499348675640469, 0.9270437520356096, 0.7729888177179459]]
nrecall_nb=[[0.9282785017770893, 0.25444272304748017, 0.8534718425369054], [0.9408548254807254, 0.2035906315501686, 0.8884636413340623], [0.9620853080568721, 0.2775904492846077, 0.8741456301831769], [0.9650018228217281, 0.2601840882165315, 0.8664904766244418], [0.9733892281053494, 0.2035906315501686, 0.8960991615020051], [0.9687414563018317, 0.18345028706825844, 0.9073095151294204], [0.977945867128406, 0.20204137428232935, 0.8802406124681006], [0.9876970746377473, 0.14626811264011666, 0.9042107181917608], [0.9905221908320423, 0.15822092599343784, 0.8938303107627814], [0.9912512530757314, 0.1659679183375866, 0.8854460949603572]]
nrecall_knn =[[0.7275293095961789, 0.8284845853234911, 0.8429222752930959], [0.7205818497611811, 0.8316326530612245, 0.8302214502822406], [0.6553408597481546, 0.8304385584020842, 0.856600086843248], [0.7138514980460269, 0.8260963960052106, 0.8452019105514547], [0.7353164694387145, 0.8485506459667789, 0.8576856274424663], [0.7437846053631527, 0.8452936706112257, 0.8617021276595744], [0.7429160786016719, 0.8457446808510638, 0.8477906850504832], [0.7474758440994463, 0.8550803300043421, 0.8561502551297362], [0.759552757273122, 0.8489849093475192, 0.8943654326348931], [0.8295701259227095, 0.8380197589838236, 0.9706872218000218]]
nrecall = []
nrecall.append(nrecall_rf)
nrecall.append(nrecall_svm)
nrecall.append(nrecall_dt)
nrecall.append(nrecall_nb)
nrecall.append(nrecall_knn)
# other(nrecall)


print("------------f1-----------")
f1_rf=[[0.6736024066182, 0.5133678537461692, 0.5908778813143698], [0.6247933884297522, 0.47433439829605967, 0.5879973027646663], [0.5697069943289225, 0.46749654218533887, 0.58201166479075], [0.7765992345544013, 0.5063402800749808, 0.5837401825514752], [0.907392527119325, 0.5535649873752555, 0.6433073389595129], [0.9026495383380169, 0.562205466540999, 0.6323241123938139], [0.9034448327508737, 0.5428331130601947, 0.6230636833046471], [0.9043460804978419, 0.5552456033959975, 0.6359007001909612], [0.8744455159112826, 0.5928212162780064, 0.6535932362611555], [0.8020411754355095, 0.5525902668759811, 0.6930612244897961]]
f1_svm=[[0.5080332409972299, 0.4108698176750667, 0.5797543413807709], [0.5005583472920156, 0.3947786606129398, 0.5980106328245584], [0.421618916551983, 0.3791323448654585, 0.5818940975517176], [0.6995384442192952, 0.4404054526389375, 0.592723697148476], [0.8464006416683376, 0.47925420168067223, 0.655515730784548], [0.8530748258103604, 0.49716374637589816, 0.6440089814247806], [0.8433807330262367, 0.4623919494258806, 0.6266545417803375], [0.8431293881644935, 0.495008427330481, 0.6550095467792181], [0.7727941176470589, 0.42083706642774854, 0.6511575886366179], [0.6713588738702712, 0.1893590280687055, 0.6910915934755333]]
f1_dt=[[0.5319092122830441, 0.27596527985633046, 0.5156909147031588], [0.5474478792235802, 0.260622381807301, 0.5329804560260587], [0.5471349353049909, 0.28209383014029266, 0.5074135090609555], [0.5789681599115114, 0.3066108285970685, 0.48161099722657663], [0.5979657809666483, 0.2551103843008994, 0.531009506564056], [0.5930796931266634, 0.26863732337177193, 0.5133861886705733], [0.5901176470588235, 0.21307911021910017, 0.5111734980348119], [0.5810800219452935, 0.25608746065926785, 0.5191219732971261], [0.5799550422447872, 0.23485096626269245, 0.5051582241799003], [0.5823271552718603, 0.12271029699448693, 0.5130994671403198]]
f1_nb=[[0.17563245129398078, 0.48259783513738547, 0.23246542917652924], [0.15597295266716757, 0.48916737468139343, 0.1945378716534374], [0.15358148263997498, 0.5511207129354577, 0.28517917342989135], [0.17245136186770427, 0.5533815397703106, 0.19102147039687706], [0.14510433386837882, 0.5368989457444073, 0.17009526439320724], [0.13740214091707942, 0.5276461295418642, 0.15122228538942578], [0.12011814899901545, 0.5331136059326398, 0.16338104239805565], [0.08971962616822429, 0.5180825061106399, 0.1282565130260521], [0.08594418763910289, 0.5232698094282848, 0.13619167717528374], [0.09682918513467438, 0.5258811681772407, 0.12486095661846494]]
f1_knn=[[0.7326803205699021, 0.47860304968027545, 0.5368624607203287], [0.7136074531935861, 0.4634389817818817, 0.5411987232533396], [0.6792837138250022, 0.4367000380179952, 0.5111780959557901], [0.7356843575418994, 0.45974444857958074, 0.5141027220100997], [0.7801541258983462, 0.4870792890457582, 0.548577036310108], [0.7836563645887898, 0.4999378186792688, 0.5553507801941271], [0.7839581517000872, 0.477321541377132, 0.5433385864953327], [0.7864145658263306, 0.49696356275303644, 0.5718757524680953], [0.7948400777522531, 0.5943982186804172, 0.5663625851214185], [0.8446066049209467, 0.7695722356739306, 0.6133939997156264]]

f1 = []
f1.append(f1_rf)
f1.append(f1_svm)
f1.append(f1_dt)
f1.append(f1_nb)
f1.append(f1_knn)
# other(f1)

print("------------acc-----------")
acc_rf=[0.5882182660298162, 0.559849471703575, 0.5392965696917065, 0.6221595020987118, 0.7114424259969603, 0.7082579431135557, 0.700513859738004, 0.7086198161684881, 0.7172323948758775, 0.6925526525294926]
acc_svm=[0.5083948473006223, 0.507960631060935, 0.46873643074250976, 0.5797510493559126, 0.675834117391619, 0.6767749873344431, 0.658898458420786, 0.6782224795541724, 0.6339292176304553, 0.5521459072157487]
acc_dt=[0.4726443768996961, 0.4411636995223621, 0.4241568968012737, 0.5110001447387466, 0.5973076644713035, 0.6023015126293696, 0.5936889339219802, 0.5936889339219802, 0.6028805095172614, 0.589925454150684]
acc_nb=[0.4643218989723549, 0.472933854392821, 0.47047329570125923, 0.4838616297582863, 0.5006875588043714, 0.4956937106463053, 0.4831005283346602, 0.49026561482232034, 0.4803502931171745, 0.46623724397481364]
acc_knn=[0.599290780141844, 0.5882906354030975, 0.5615863366623245, 0.5900998697351281, 0.6277050010856192, 0.6338568430194688, 0.6243033943692553, 0.6391401896214808, 0.6685966562929724, 0.7588477961930955]
acc = []

columns=['RF-SVM','RF-DT','RF-NB','RF-KNN','SVM-DT','SVM-NB','SVM-KNN','DT-NB','DT-KNN','NB-KNN']
print(" & ".join(columns)+"\\\\")
acc.append(acc_rf)
acc.append(acc_svm)
acc.append(acc_dt)
acc.append(acc_nb)
acc.append(acc_knn)

# acc_c(acc)
# ttest_acc(acc)

train_time_rf=[23.285779754, 22.864949007, 22.766427345000004, 22.517573684, 22.73744656400001, 23.128049393000012, 22.54622195500002, 23.03468951299999, 23.10191178400001, 22.43214451999998]
train_time_svm=[19.583422667999997, 23.666526994000037, 20.264216262000048, 21.536675108999987, 22.13041376299998, 25.097001312999964, 23.461098671000002, 24.391538777999983, 24.69801843800002, 25.030781767999997]
train_time_dt=[2.0108925670000417, 2.1086051899999916, 2.08406729699999, 1.981955620000008, 2.0281113629999936, 2.014338001999988, 2.055588300000011, 2.0880680610000013, 2.080528435999952, 1.9817313810000314]
train_time_nb=[0.19475857600002655, 0.1821556829999622, 0.19069197999999687, 0.2064110730000266, 0.2503150279999886, 0.2176910289999796, 0.19954548800001248, 0.21253632100001596, 0.1857033389999856, 0.22316738899996835]
train_time_knn =[56.008723358, 57.869172299000184, 56.575313815999834, 51.11617378600022, 53.50785209800006, 59.92061892000038, 56.902158822000274, 58.15772834499967, 56.840582400999665, 60.241993315999935]
train_time = []
train_time.append(train_time_rf)
train_time.append(train_time_svm)
train_time.append(train_time_dt)
train_time.append(train_time_nb)
train_time.append(train_time_knn)

test_time_rf=[0.5592228620000022, 0.5794928139999982, 0.6047780289999878, 0.6056809699999945, 0.5737205260000025, 0.5546365069999979, 0.5938832029999901, 0.5449833849999948, 0.5569488749999891, 0.5426545709999857]
test_time_svm=[0.027325085999962084, 0.017684690999999475, 0.018056318999981613, 0.017658729000004314, 0.018158556000003045, 0.017771349999975428, 0.017234480000013264, 0.01775730700001077, 0.01745749600002, 0.01741958700000623]
test_time_dt=[0.009666461999984222, 0.010213727000007111, 0.009639068000012685, 0.010184701000014229, 0.00953860699996767, 0.011277083000038601, 0.009413447999975233, 0.009720874999970874, 0.00957377100002077, 0.00956181800000877]
test_time_nb=[0.020212474000004477, 0.019088431000000128, 0.02142839800001184, 0.020244171999991067, 0.022005125000021053, 0.019223939000028167, 0.019263447000014366, 0.0212922100000128, 0.021251178999989406, 0.022099278999974103]
test_time_knn = [346.04603020900004, 335.80494536599986, 334.12987780500043, 316.1399803950003, 330.7274657570001, 279.3862287410002, 277.8007801719996, 276.3815795069995, 278.6001866609995, 311.9531824220003]

test_time = []
test_time.append(test_time_rf)
test_time.append(test_time_svm)
test_time.append(test_time_dt)
test_time.append(test_time_nb)
test_time.append(test_time_knn)

# df = pd.DataFrame()
# df['model'] = ['Random Forest','SVM','Decision Tree','Naive Bayesian','KNN']
# train_mean = np.average(train_time,axis =1)
# df['train_time'] =train_mean
# test_mean = np.average(test_time,axis =1)
# df['test_time'] =test_mean

# ax = df.plot.bar(rot=0,x='model')
# ax.set_ylabel("running time(s)")

# for vid, value in enumerate(train_mean): 
#     ax.text(vid-0.2,value, str(np.around(value,2)))

# for vid, value in enumerate(test_mean): 
#     ax.text(vid+0.05,value, str(np.around(value,2)))


# from scipy.stats import friedmanchisquare

# data1 = [2,3,4,5,1]
# data2 = [1,3,4,5,2]

# data=[data1,data2]
# data=np.array(data)

# r1=data.mean()
# n=4
# k=3
# t1=n* np.sum((data.mean(axis=0)-r1)* (data.mean(axis=0)-r1))
# t2=(1/(n*(k-1)))*np.sum((data-r1) * (data-r1))

# print(t1/t2)

# data1 = [2,1]
# data2 = [3,3]
# data3 = [4,4]
# data4 = [5,5]
# data5 = [1,2]
# stat, p = friedmanchisquare(data1, data2,data3,data4,data5)
# print(stat)
# print(p)

# from Orange.evaluation import compute_CD,graph_ranks
# import matplotlib.pyplot as plt
# names = ["Random Forest", "SVM", "Decision Tree","Naive Bayesian","KNN" ]
# avranks =  [1.5, 3,4,5, 1.5]
# cd = compute_CD(avranks, 2) #tested on 4 datasets
# print(cd)
# graph_ranks(avranks, names, cd=cd, width=6, textspace=1.5)

print("------------recall2-----------")

recall2_st = [[0.7320725417336809, 0.8528237931223006, 0.551461598310548],[0.7271365980810826, 0.8470832649937128, 0.5352339668778482],[0.7211469136487161, 0.8405226614181838, 0.5125597421362676],[0.6912539515279241, 0.8122027226504839, 0.44653773480048903],[0.41961067051189616, 0.8501448799956263, 0.05885295098366122],[0.09245188841439743, 0.9285440927231972, 0.002723129932199622]]
recall2_lp = [[0.4384116244246021, 0.9378382811218632, 0.48660664665999775], [0.41334368587432757, 0.9342299491553223, 0.4933311103701234], [0.37707281903388606, 0.9243343720955661, 0.4789374235856397], [0.9837502079751539, 0.05319556065824722, 0.00944759364232522], [0.9999445399589596, 0.0007654037504783774, 0.0], [1.0, 0.0, 0.0]]
recall2_ls = [[0.3724141755864899, 0.9370728773713848, 0.5145048349449817], [0.369973933780711, 0.9337379038871576, 0.5062242969878848], [0.35699628417725027, 0.9272319720080914, 0.48543959097476935], [0.33148466529865234, 0.8891804712700235, 0.43664554851617204], [0.28073872774665853, 0.6359411732546061, 0.3350561298210515], [0.31584493372525096, 0.4253457984801268, 0.2952650883627876]]

recall2 = []
recall2.append(recall2_st)
recall2.append(recall2_lp)
recall2.append(recall2_ls)
other2(recall2)


print("------------nrecall2-----------")
nrecall2_st = [[0.806145790271462, 0.9136433032616239, 0.8499807279334839],[0.8019567314317211, 0.9075364330326162, 0.846842134243709],[0.7996141656331818, 0.8952116585704372, 0.8438962612190959],[0.7937439713380184, 0.8504371963913948, 0.8323605528329938],[0.8088190712415598, 0.39100624566273423, 0.9651726226529376],[0.9262505167424555, 0.08677307425399028, 0.9988712075326248]]
nrecall2_lp = [[0.8809700978365715, 0.7050659264399722, 0.8470073233852762], [0.8888521427587157, 0.6930742539902846, 0.8400969109630527], [0.8905332782141381, 0.6682303955586398, 0.8329387148284786], [0.03786688714344771, 0.9892019430950728, 0.9962832443147404], [0.00041339396444811904, 0.9999444829979182, 1.0], [0.0, 1.0, 1.0]]
nrecall2_ls = [[0.9058288548987184, 0.6818043025676613, 0.8259181763118771], [0.9046713517982637, 0.6729493407356003, 0.8288640493364903], [0.9018602728400166, 0.6575711311589174, 0.8269093111612796], [0.890340361030729, 0.6230673143650243, 0.8166400528605253], [0.8161499242111065, 0.5678278972935461, 0.7424976598204944], [0.70549813972716, 0.5893962526023595, 0.723308187875117]]

nrecall2 = []
nrecall2.append(nrecall2_st)
nrecall2.append(nrecall2_lp)
nrecall2.append(nrecall2_ls)
other2(nrecall2)


print("------------f12----------------")
f12_st = [[0.6899255194041554, 0.8431664009080835, 0.5947970988431337],[0.6841473596326446, 0.8348960017243238, 0.580390502591298],[0.6789192011486752, 0.8212606837606838, 0.5608903214035942],[0.6563627267700571, 0.7710393149085247, 0.5003424870788966],[0.46511341980697113, 0.5575475080674077, 0.10424254355743676],[0.1490122463573791, 0.49825446651216004, 0.005419155054191552]]
f12_lp = [[0.5225582548339117, 0.7446928586932928, 0.5420497105890364], [0.5049971203035539, 0.7359807046257213, 0.5432846782337281], [0.47211999166724533, 0.7171580063626725, 0.5274173806609547], [0.5019241652518392, 0.09901796163435607, 0.018580250286900926], [0.49854142760365544, 0.0015294696017916646, 0.0], [0.4984588165369676, 0.0, 0.0]]
f12_ls = [[0.47686681106416223, 0.7310103637992068, 0.551481757259866], [0.4737757892120309, 0.7244231421784866, 0.5467751132987184], [0.4593100003567733, 0.7127997142076617, 0.5291373879331234], [0.42712688033729945, 0.6757801138488387, 0.4833440989203654], [0.34014245397124043, 0.5113866174272399, 0.3612775647171621], [0.3309891898175056, 0.3807845728409564, 0.31855382678298405]]

f12 = []
f12.append(f12_st)
f12.append(f12_lp)
f12.append(f12_ls)
other2(f12)


print("------------acc2---------------")
acc2_st =[0.7129022755725754,0.7039546358347448,0.6922453788938803,0.6509131747551367,0.4450806392223286,0.3442816113115841]
acc2_lp =[0.6225605714706532, 0.6152514912732896, 0.5951100964724942, 0.3476139627365785, 0.3322041387436483, 0.331964798586052]
acc2_ls =[0.6096362029604536, 0.6049598644966493, 0.5915752264526106, 0.5541276971794683, 0.41834818469695856, 0.3459017600706974]

acc2 = []
acc2.append(acc2_st)
acc2.append(acc2_lp)
acc2.append(acc2_ls)
acc_c2(acc2)
ttest_acc2(acc2)

train_time2_st=[28.415089754999997,2131.896679208,2762.7472615449997,3951.270158694,5918.986796524001,385.2241754179995]
train_time2_lp=[5524.40625, 5517.546875, 5516.21875, 5510.40625, 5511.359375, 5525.9375]
train_time2_ls=[5577.546875, 5511.0, 5479.828125, 5491.6875, 5491.78125, 5516.625]

train_time2 = []
train_time2.append(train_time2_st)
train_time2.append(train_time2_lp)
train_time2.append(train_time2_ls)

test_time2_st=[2.302970533,3.2618691200000285,2.8510130220001884,1.715419309999561,1.4250788670015027,0.7796331050012668]
test_time2_lp=[2764.6875, 2767.625, 2763.734375, 2758.953125, 2762.546875, 2764.953125]
test_time2_ls=[2766.15625, 2760.25, 2751.5, 2750.625, 2762.09375, 2761.765625]

test_time2 = []
test_time2.append(test_time2_st)
test_time2.append(test_time2_lp)
test_time2.append(test_time2_ls)

df2 = pd.DataFrame()
df2['model'] = ['Self Training','LabelPropagation with KNN','LabelSpreading With KNN']
train_mean2 = np.average(train_time2,axis =1)
df2['train_time'] =train_mean2
test_mean2 = np.average(test_time2,axis =1)
df2['test_time'] =test_mean2

ax = df2.plot.bar(rot=0,x='model')
ax.set_ylabel("running time(s)")

for vid, value in enumerate(train_mean2): 
    ax.text(vid-0.2,value, str(np.around(value,2)))

for vid, value in enumerate(test_mean2): 
    ax.text(vid+0.02,value, str(np.around(value,2)))
plt.show()


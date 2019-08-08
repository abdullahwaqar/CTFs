#!/usr/bin/env python

from pwn import *
import os

context.log_level = 'critical'
elf = ELF('./be-quick-or-be-dead-2')

number = 4368447739709774716003881551397205159088952756411141941533814668901464054869881997817744932743716769887780898920209866426445447485522551760777962122217963045451173078851717190916177144613851841799958503738854017612313939353
7068296920928069200976659859017770655917388445979256581929916714916448248156756764906037038490673848085929558616817651916362667405541400507025189054254169424143720600260649508727230257081773103163754279823569485320791872016
11436744660637843916980541410414975815006341202390398523463731383817912303026638762723781971234390617973710457537027518342808114891063952267803151176472132469594893679112366699643407401695624944963712783562423502933105811369
18505041581565913117957201269432746470923729648369655105393648098734360551183395527629819009725064466059640016153845170259170782296605352774828340230726301893738614279373016208370637658777398048127467063385992988253897683385
29941786242203757034937742679847722285930070850760053628857379482552272854210034290353600980959455084033350473690872688601978897187669305042631491407198434363333507958485382908014045060473022993091179846948416491187003494754
48446827823769670152894943949280468756853800499129708734251027581286633405393429817983419990684519550092990489844717858861149679484274657817459831637924736257072122237858399116384682719250421041218646910334409479440901178139
78388614065973427187832686629128191042783871349889762363108407063838906259603464108337020971643974634126340963535590547463128576671943962860091323045123170620405630196343782024398727779723444034309826757282825970627904672893
126835441889743097340727630578408659799637671849019471097359434645125539664996893926320440962328494184219331453380308406324278256156218620677551154683047906877477752434202181140783410498973865075528473667617235450068805851032
205224055955716524528560317207536850842421543198909233460467841708964445924600358034657461933972468818345672416915898953787406832828162583537642477728171077497883382630545963165182138278697309109838300424900061420696710523925
332059497845459621869287947785945510642059215047928704557827276354089985589597251960977902896300963002565003870296207360111685088984381204215193632411218984375361135064748144305965548777671174185366774092517296870765516374957
537283553801176146397848264993482361484480758246837938018295118063054431514197609995635364830273431820910676287212106313899091921812543787752836110139390061873244517695294107471147687056368483295205074517417358291462226898882
869343051646635768267136212779427872126539973294766642576122394417144417103794861956613267726574394823475680157508313674010777010796924991968029742550609046248605652760042251777113235834039657480571848609934655162227743273839
1406626605447811914664984477772910233611020731541604580594417512480198848617992471952248632556847826644386356444720419987909868932609468779720865852689999108121850170455336359248260922890408140775776923127352013453689970172721
2275969657094447682932120690552338105737560704836371223170539906897343265721787333908861900283422221467862036602228733661920645943406393771688895595240608154370455823215378611025374158724447798256348771737286668615917713446560
3682596262542259597597105168325248339348581436377975803764957419377542114339779805861110532840270048112248393046949153649830514876015862551409761447930607262492305993670714970273635081614855939032125694864638682069607683619281
5958565919636707280529225858877586445086142141214347026935497326274885380061567139769972433123692269580110429649177887311751160819422256323098657043171215416862761816886093581299009240339303737288474466601925350685525397065841
9641162182178966878126331027202834784434723577592322830700454745652427494401346945631082965963962317692358822696127040961581675695438118874508418491101822679355067810556808551572644321954159676320600161466564032755133080685122
15599728101815674158655556886080421229520865718806669857635952071927312874462914085401055399087654587272469252345304928273332836514860375197607075534273038096217829627442902132871653562293463413609074628068489383440658477750963
25240890283994641036781887913283256013955589296398992688336406817579740368864261031032138365051616904964828075041431969234914512210298494072115494025374860775572897437999710684444297884247623089929674789535053416195791558436085
40840618385810315195437444799363677243476455015205662545972358889507053243327175116433193764139271492237297327386736897508247348725158869269722569559647898871790727065442612817315951446541086503538749417603542799636450036187048
66081508669804956232219332712646933257432044311604655234308765707086793612191436147465332129190888397202125402428168866743161860935457363341838063585022759647363624503442323501760249330788709593468424207138596215832241594623133
106922127055615271427656777512010610500908499326810317780281124596593846855518611263898525893330159889439422729814905764251409209660616232611560633144670658519154351568884936319076200777329796097007173624742139015468691630810181
173003635725420227659876110224657543758340543638414973014589890303680640467710047411363858022521048286641548132243074630994571070596073595953398696729693418166517976072327259820836450108118505690475597831880735231300933225433314
279925762781035499087532887736668154259249042965225290794871014900274487323228658675262383915851208176080970862057980395245980280256689828564959329874364076685672327641212196139912650885448301787482771456622874246769624856243495
452929398506455726747408997961325698017589586603640263809460905203955127790938706086626241938372256462722518994301055026240551350852763424518358026604057494852190303713539455960749100993566807477958369288503609478070558081676809

# for key, adress in elf.symbols.iteritems():
#     print key, hex(adress)

elf.asm(elf.symbols['alarm'], 'ret')
elf.asm(elf.symbols['calculate_key'], 'mov eax,%s\nret\n' %(hex(number & 0xFFFFFFFF)))
elf.save('./new')
os.system('chmod +x ./new')
p = process('./new')
p.poll(True)
print p.recvall().split('\n')[-2]
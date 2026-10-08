from pathlib import Path
from html import escape as e
ROOT=Path(__file__).resolve().parents[1]
WHITE='#eee8e2'; MUTED='#b7aaa4'; RED='#f01818'
def text(x,y,s,size=24,color=WHITE,weight=400,mono=False,spacing=0):
 return f'<text x="{x}" y="{y}" fill="{color}" font-family="{("monospace" if mono else "Arial,Helvetica,sans-serif")}" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">{e(s)}</text>'
def lines(x,y,ss,size=24,color=MUTED,gap=35):
 return ''.join(text(x,y+i*gap,s,size,color) for i,s in enumerate(ss))
def rect(x,y,w,h,fill='#111011',stroke='#776b6555',r=0):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>'
def path(d,stroke=RED,width=2,fill='none',extra=''):
 return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" {extra}/>'
def circle(x,y,r,fill='none',stroke=RED,width=2):
 return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
def label(x,y,s):return text(x,y,s,19,RED,500,True,1.2)
def grid(x,y,w,h):
 return rect(x,y,w,h,'url(#grid)','none')
def formation(x,y,scale):
 s=grid(0,0,480,300)
 s+=path('M35 240Q126 233 172 173T330 146Q384 140 445 58','#c5b9b0',2,extra='stroke-dasharray="7 8"')
 s+=circle(285,91,43,stroke='#766f6b')+circle(285,91,26,stroke='#766f6b')
 for i,(dx,dy) in enumerate([(240,67),(178,117),(300,117),(118,164),(360,164),(55,213),(420,213)]):
  c=RED if i==0 else '#d7cdc5'
  s+=f'<g transform="translate({dx} {dy})">'+path('M-18-13L18 13M-18 13L18-13',c,3)
  for a,b in [(-18,-13),(-18,13),(18,-13),(18,13)]:s+=circle(a,b,7,'#0c0b0c',c)
  s+=rect(-5,-7,10,14,c,'none',2)+'</g>'
 s+=label(12,285,'DRAW → COORDINATE → AVOID')
 return f'<g transform="translate({x} {y}) scale({scale})">{s}</g>'
def arm(x,y,scale):
 s=grid(0,0,420,260)
 s+=path('M53 223H247V244H53ZM118 222V169H150V222M134 169L209 94L234 120L154 192M209 94L265 54L282 77L234 120M272 64L323 100M272 64L294 31','#d8cdc6',7)
 for a,b in [(134,169),(222,109),(273,64)]:s+=circle(a,b,12,'#151214',RED,3)+circle(a,b,4,RED,RED)
 s+=path('M345 65H390V117H345Z M347 91H386',RED,2)+path('M293 113L351 157M304 97L366 140','#a2958b',2,extra='stroke-dasharray="5 7"')
 s+=label(22,35,'PARTS + JOINTS = ROBOT')
 return f'<g transform="translate({x} {y}) scale({scale})">{s}</g>'
def hand(x,y,scale):
 s=grid(0,0,420,260)
 s+=path('M44 25H81M44 25V62M373 25H336M373 25V62M44 232H81M44 232V195M373 232H336M373 232V195','#776e68',2)
 s+=path('M208 230L202 165L158 139L125 121L100 108M202 165L175 116L165 70L158 37M202 165L211 108L213 59L212 25M202 165L242 119L267 77L281 45M202 165L267 147L301 124L325 105','#dbd0c8',4)
 for a,b in [(202,165),(158,139),(125,121),(100,108),(175,116),(165,70),(158,37),(211,108),(213,59),(212,25),(242,119),(267,77),(281,45),(267,147),(301,124),(325,105)]:s+=circle(a,b,4,RED,RED)
 s+=path('M54 152H363',RED,1,extra='stroke-opacity=".4"')
 return f'<g transform="translate({x} {y}) scale({scale})">{s}</g>'
def tob(x,y,scale):
 s=rect(10,310,510,18,'#484144','#71645c',3)+rect(18,328,494,10,'#171415','none')
 s+=path('M260 311V244','#79706b',8)+path('M140 135C110 240 232 289 327 241M163 48C243-23 370 59 372 153','#7d746f',3)
 s+='<g filter="url(#glow)">'+path('M143 111C170 39 247 48 314 72S366 194 297 231S197 166 157 166S132 140 143 111Z','#ff2a3d',2,'url(#membrane)')+path('M196 55C277 20 363 118 324 194S235 276 191 189S120 88 196 55Z','#f64248',3,'url(#membrane)')+'</g>'
 s+=path('M157 168C137 102 251 85 283 99S352 221 283 234S209 223 157 168Z','#edc5c4',1.4,'url(#membrane)')
 s+=path('M244 217Q185 252 96 284M244 217Q307 254 420 279M244 217Q270 264 260 289',RED,1.5,extra='stroke-opacity=".7"')
 s+=rect(36,253,114,69,'#292527','#8b8077',3)+rect(43,259,100,54,'#070708','#49413d')+path('M34 322H155L167 330H25Z','#8b8077',2,'#383132')
 s+=circle(91,285,14,stroke=RED)+text(57,274,'LOCAL CORE',8,MUTED,400,True)
 s+=rect(407,248,47,77,'#171415','#8b8077',4)+rect(412,254,37,64,'#080708','#49413d',2)+circle(430,284,11,stroke=RED)+text(418,307,'PLANNED',6,MUTED,400,True)
 s+=rect(245,267,26,70,'#343031','none',3)+circle(258,298,24,'#5b5350','#8b8077')+circle(258,298,20,'#090808','#8b8077',1)+circle(258,300,10,stroke=RED)+text(247,289,'10:09',6,WHITE,400,True)
 return f'<g transform="translate({x} {y}) scale({scale})">{s}</g>'
def defs():
 return '''<defs>
 <linearGradient id="case" x2="1" y2="1"><stop stop-color="#5a5756"/><stop offset=".2" stop-color="#252729"/><stop offset=".75" stop-color="#222426"/><stop offset="1" stop-color="#69625d"/></linearGradient>
 <radialGradient id="screen"><stop stop-color="#211b1d"/><stop offset="1" stop-color="#090809"/></radialGradient>
 <radialGradient id="membrane"><stop stop-color="#ff203000"/><stop offset=".7" stop-color="#ff203012"/><stop offset="1" stop-color="#ff203050"/></radialGradient>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#c7b6aa" stroke-opacity=".07"/></pattern>
 <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><path d="M0 3H4" stroke="#000" stroke-opacity=".2"/></pattern>
 <filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 </defs>'''
def shell(w,h):
 s=rect(0,0,w,h,'#050505','none')+rect(10,10,w-20,h-20,'url(#case)','#817a75',32)+rect(18,18,w-36,h-36,'none','#141315',26)+rect(36,68,w-72,h-132,'#080708','#94867d',32)+rect(44,76,w-88,h-148,'url(#screen)','#050505',28)
 for x in [32,w-32]:s+=circle(x,38,7,'#202123','#8d837c',1)+path(f'M{x-3} 41L{x+3} 35','#090909',2)
 s+=text(w/2,43,'DH-06 / PERSONAL SYSTEMS TERMINAL',16,MUTED,500,True,1).replace('letter-spacing="1"','letter-spacing="1" text-anchor="middle"')
 for x in range(54,int(w*.35),8):s+=rect(x,h-43,3,15,'#090909','none')
 s+=circle(w-138,h-33,4,RED,RED)+text(w-126,h-28,'PWR',14,MUTED,400,True)+circle(w-49,h-32,13,'#292729','#92847b',3)
 return s
def card(x,y,w,h):return rect(x,y,w,h,'#111011','#665952',3)+path(f'M{x} {y}H{x+70}',RED,3)
def build(mobile):
 w,h=(600,3270) if mobile else (1200,1990)
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">Devashish Harsh — robotics lab terminal</title><desc id="desc">A continuous monitor exhibit showcasing solo robotics research, MDOFS, RoboSnap, HandBot, TOB, engineering specialities and confidential work at Invictron. Repository links and accessible project notes follow this display.</desc>'+defs()+shell(w,h)
 if not mobile:
  s+=label(80,125,'SYSTEM PROFILE / RESEARCH &amp; BUILD LOG'.replace('&amp;','&'))+text(960,125,'INVIC­TRON'.replace('\u00ad',''),19,MUTED,400,True)
  s+=text(76,224,'DEVASHISH',82,WHITE,900,False,-5)+text(76,301,'HARSH.',82,RED,900,False,-5)
  s+=lines(82,350,['Robotics systems engineer.','Solo research. Working tools. Tested ideas.'],24)
  s+=text(765,203,'BUILD.',50,WHITE,900)+text(765,259,'TEST.',50,WHITE,900)+text(765,315,'VALIDATE.',50,RED,900)
  s+=path('M80 395H1120','#76655d',1)+label(80,432,'01 / SELECTED BUILDS')+text(925,432,'SOLO PROJECTS',18,MUTED,400,True)
  s+=card(80,457,1040,335)+label(106,493,'MDOFS / MULTI-DRONE PX4 + RL')+text(103,561,'DRAW THE',52,WHITE,900,False,-2)+text(103,615,'FORMATION.',52,RED,900,False,-2)
  s+=text(106,670,'86%',48,WHITE,900)+text(254,671,'100 SIMULATION EPISODES',18,MUTED,400,True)
  s+=lines(106,713,['13 drones including the leader. PPO preferred.','PyBullet training → ROS 2 / Gazebo validation.'],21,gap=32)+formation(620,494,1)
  for x in [80,620]:s+=card(x,820,500,380)
  s+=label(104,857,'02 / ROBOSNAP')+text(104,904,'ROBOT PARTS.',40,WHITE,900,False,-1)+arm(107,920,.67)+lines(104,1133,['Fixed attachments. Reusable joint parts.','Assemble arms and rovers. Export URDF.'],21,gap=31)
  s+=label(644,857,'03 / HANDBOT')+text(644,904,'HUMAN MOTION.',40,WHITE,900,False,-1)+hand(689,923,.64)+lines(644,1133,['MediaPipe → simulated hand in PyBullet.','88% gesture accuracy in a later run.'],21,gap=31)
  s+=path('M80 1231H1120','#76655d',1)+label(80,1268,'04 / TOB — THE ORDINARY BEING')
  s+=text(78,1360,'TOB.',88,WHITE,900,False,-5)+lines(83,1408,['A personal working partner.','Local model + tools on my computer.','ESP32 watch gateway over Wi-Fi.'],24,gap=36)
  s+=lines(83,1542,['ROS 2 nodes / topics / programs / processes'],20,gap=30)+text(83,1580,'WEB / ANDROID / ROS-EDGE: PLANNED',17,RED,400,True)
  s+=tob(604,1284,.96)
  s+=path('M80 1640H1120','#76655d',1)+label(80,1677,'05 / ENGINEERING STACK')
  for x,y,name,tools in [(80,1720,'AUTONOMY','PX4 / ROS 2 / SAC / PPO'),(440,1720,'PERCEPTION','OpenCV / MediaPipe / LiDAR'),(800,1720,'SIMULATION','URDF / Gazebo / PyBullet'),(80,1810,'MECHANICAL','Fusion 360 / Ansys / FEA'),(440,1810,'SOFTWARE','Python / bridges / PID'),(800,1810,'EMBEDDED','ESP32 / Arduino / RPi')]:
   s+=text(x,y,name,24,WHITE,700)+text(x,y+30,tools,18,MUTED,400,True)
  s+=text(80,1892,'INVIC­TRON / PRIVATE UAV SYSTEMS'.replace('\u00ad',''),18,RED,500,True)+text(650,1892,'BUILDING & TESTING / NO INTERNAL DETAILS',16,MUTED,400,True)
 else:
  s+=label(72,130,'RESEARCH / TOOLS / ROBOTICS')+text(68,208,'DEVASHISH',62,WHITE,900,False,-3)+text(68,269,'HARSH.',62,RED,900,False,-3)
  s+=lines(73,315,['Robotics systems engineer at Invictron.','Solo research for people who build,','test and validate robotic systems.'],25,gap=37)
  s+=path('M72 423H528','#76655d',1)+label(72,463,'01 / MDOFS')+text(69,526,'DRAW THE',54,WHITE,900,False,-2)+text(69,582,'FORMATION.',54,RED,900,False,-2)
  s+=formation(76,612,.92)
  s+=text(73,960,'86%',68,WHITE,900)+lines(245,925,['100 simulation','episodes'],23,gap=34)
  s+=lines(73,1006,['13 drones including the leader.','Explored SAC; PPO performed best.','PyBullet training. ROS 2 + Gazebo','validation. User-drawn formations.'],24,gap=36)
  s+=path('M72 1147H528','#76655d',1)+label(72,1187,'02 / ROBOSNAP')+text(69,1250,'ROBOT PARTS.',48,WHITE,900,False,-2)+arm(84,1274,1.04)
  s+=lines(73,1588,['Fixed attachments and reusable joints.','Arms, rovers and modular assemblies.','Build in the browser. Export URDF.'],24,gap=36)
  s+=path('M72 1700H528','#76655d',1)+label(72,1740,'03 / HANDBOT')+text(69,1803,'HUMAN MOTION.',46,WHITE,900,False,-2)+hand(93,1827,1)
  s+=lines(73,2129,['MediaPipe tracks and maps the hand','to a robotic hand in PyBullet.','88% gesture accuracy in a later run.'],24,gap=36)
  s+=path('M72 2240H528','#76655d',1)+label(72,2280,'04 / THE ORDINARY BEING')+text(69,2361,'TOB.',79,WHITE,900,False,-3)+tob(78,2384,.84)
  s+=lines(73,2706,['A personal working partner.','Local model + tools on my computer.','ESP32 watch gateway over Wi-Fi.','ROS 2 nodes, topics and processes.'],24,gap=36)
  s+=text(73,2870,'WEB / ANDROID / ROS-EDGE: PLANNED',18,RED,400,True)
  s+=path('M72 2905H528','#76655d',1)+label(72,2946,'05 / ENGINEERING STACK')
  s+=lines(73,2990,['PX4 · ROS 2 · Gazebo · PyBullet','OpenCV · MediaPipe · URDF · Python','Fusion 360 · Ansys · FEA · Embedded'],24,gap=38)
  s+=text(73,3138,'PRIVATE UAV WORK AT INVIC­TRON'.replace('\u00ad',''),19,RED,400,True)+text(73,3175,'BUILDING & TESTING / DETAILS WITHHELD',18,MUTED,400,True)
 s+=rect(46,78,w-92,h-152,'url(#scan)','none',26)+'</svg>'
 return s
for mobile,name in [(True,'lab-console-mobile.svg')]:
 (ROOT/'assets'/name).write_text(build(mobile))

# Individual frames for the desktop display and reduced-motion still.
from types import SimpleNamespace
m=SimpleNamespace(**globals())
ROOT=ROOT/'assets'
for i in range(4):
 w,h=1200,830
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">Devashish Harsh — project display {i+1}</title><desc id="desc">Original robotics portfolio terminal. Selected research project, schematic and evaluation notes.</desc>'+m.defs()+m.shell(w,h)
 s+=m.text(74,134,'DEVASHISH HARSH.',38,m.WHITE,900,False,-1)+m.text(75,172,'ROBOTICS SYSTEMS ENGINEER / INVIC­TRON'.replace('\u00ad',''),18,m.MUTED,400,True)
 s+=m.text(1000,132,f'0{i+1} / 04',23,m.RED,500,True)+m.path('M75 203H1125','#76655d',1)
 if i==0:
  s+=m.label(78,248,'01 / MDOFS · SOLO SIMULATION')+m.text(74,337,'DRAW THE',63,m.WHITE,900,False,-2)+m.text(74,406,'FORMATION.',63,m.RED,900,False,-2)
  s+=m.text(78,495,'86%',75,m.WHITE,900)+m.lines(266,462,['SUCCESS / 100','SIMULATION EPISODES'],18,gap=31)
  s+=m.lines(80,554,['13 drones including the leader.','User-drawn formations. PPO preferred.','PyBullet training → ROS 2 + Gazebo.'],24,gap=36)+m.formation(615,285,1.02)
 elif i==1:
  s+=m.label(78,248,'02 / ROBOSNAP · SOLO TOOL')+m.text(74,337,'ROBOT',63,m.WHITE,900,False,-2)+m.text(74,406,'FROM PARTS.',63,m.RED,900,False,-2)
  s+=m.lines(80,482,['Fixed attachments connect the parts.','Reusable joint parts provide motion.','Arms, rovers and other assemblies.'],24,gap=36)
  s+=m.text(80,635,'BUILD → INSPECT → EXPORT URDF',20,m.RED,500,True)+m.arm(647,324,1.06)
 elif i==2:
  s+=m.label(78,248,'03 / HANDBOT · SOLO RESEARCH')+m.text(74,337,'HAND IN',63,m.WHITE,900,False,-2)+m.text(74,406,'VIRTUAL SPACE.',60,m.RED,900,False,-2)
  s+=m.lines(80,482,['MediaPipe camera tracking.','Hand motion mapped into PyBullet.','88% gesture accuracy in a later run.'],24,gap=36)
  s+=m.text(80,635,'TRACK → MAP → INTERACT',20,m.RED,500,True)+m.hand(673,305,1)
 else:
  s+=m.label(78,248,'04 / TOB · IN DEVELOPMENT')+m.text(74,353,'TOB.',90,m.WHITE,900,False,-4)+m.text(78,400,'THE ORDINARY BEING',22,m.RED,500,True,1)
  s+=m.lines(80,478,['A personal working partner.','Local model + connected tools.','ESP32 watch gateway over Wi-Fi.','ROS 2 nodes, topics and processes.'],24,gap=36)
  s+=m.text(80,650,'WEB / ANDROID / ROS-EDGE: PLANNED',18,m.RED,400,True)+m.tob(608,283,.98)
 s+=m.path('M75 692H1125','#76655d',1)
 for n,(x,name) in enumerate([(80,'01 / MDOFS'),(350,'02 / ROBOSNAP'),(630,'03 / HANDBOT'),(910,'04 / TOB')]):
  s+=m.rect(x-9,710,220,39,m.RED if i==n else '#191617','#5e514b',2)+m.text(x,737,name,17,m.WHITE if i==n else m.MUTED,500,True)
 s+=m.rect(46,78,w-92,h-152,'url(#scan)','none',26)+'</svg>'
 (ROOT/f'lab-display-{i+1}.svg').write_text(s)
(ROOT/'lab-display.svg').write_text((ROOT/'lab-display-1.svg').read_text())

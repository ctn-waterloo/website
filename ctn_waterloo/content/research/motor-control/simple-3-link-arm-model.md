title: Simple 3-link arm model

To run, download the attached .zip file, extract the .mdl, and past this code
into a script file. This simulation was made by creating a model in MapleSim
4, exporting to C, and then importing into simulink. Created in Matlab
7.7.0471 (R2008b).  %% This is a simple 3-link arm model created by designing
an arm in %% MapleSim4, exporting to C, and then importing into Matlab. clear;
close all; % Constants dt = .2; L1 = 3.1; L2 = 2.7; L3 = 1.5; % Initial
torques tau1 = 0; tau2 = 0; tau3 = 0; % Set up initial state of the model %
[ElbowAngle WristAngle WristVelocity ElbowVelocity ShoulderAngle %
ShoulderVelocity] armState = [pi/2 pi/2 0 0 pi/2 0]; % Load in the simulink
model mdl = load_system('MapleSim_TorqueArm1');
set_param(mdl,'SaveFinalState','on', 'FinalStateName', ['armState'],
'LoadInitialState', 'on', ... 'InitialState',['armState']); [t,x,y] =
sim('MapleSim_TorqueArm1',[0 dt],[],[0 tau1 tau2 tau3]); ch = ''; keydown=0; %
Set up figure and character input figure(1); clf; hold on; grid; set(gca,
'NextPlot', 'replacechildren'); set(gcf,'doublebuffer','on');
set(gcf,'KeyPressFcn','keydown=1;'); t = 0; % set start time while 1==1 %for i
= dt:dt:endTime t = t+dt; set_param(mdl, 'InitialState',['armState']);
[t1,x,y] = sim('MapleSim_TorqueArm1',[t t+dt],[],[t tau1 tau2 tau3]); %%
Keyboard Control ch = get(gcf,'CurrentCharacter'); if keydown==1 switch(ch)
case 'q' %shoulder left tau1=tau1+.1; case 'w' %shoulder right tau1 = tau1-.1;
case 'e' % set negative! tau1 = -tau1; case 'r' % set to 0! tau1 = 0; case 'o'
%elbow left tau2 = tau2+.1; case 'p' tau2 = tau2-.1; case 'u' % set negative!
tau2 = -tau2; case 'y' % set to O! tau2 = 0; case 'f' tau3 = tau3+.1; case 'g'
tau3 = tau3-.1; case 'h' tau3 = -tau3; case 'j' tau3 = 0; end keydown=0; end
%% Plot the arm and torques S1 = sin(x(1)); C1 = cos(x(1)); C12 =
cos(x(1)+x(2)); S12 = sin(x(1)+x(2)); C123 = cos(x(1)+x(2)+x(3)); S123 =
sin(x(1)+x(2)+x(3)); x1 = L1*C1; y1 = L1*S1; %xy of elbow x2 = x1+L2*C12; y2 =
y1 + L2*S12; %xy of hand x3 = x2 + L3*C123; y3 = y2 + L3*S123; %xy of finger
clf; hold on; axis([-5 5 -5 5]); grid; plot([0 x1],[0 y1]); %plot shoulder to
elbow plot([x1 x2],[y1,y2]) %plot elbow to wrist plot([x2 x3],[y2 y3]) % plot
wrist to finger plot(x3,y3,'ro'); %plot finger % print the torques
text(2,-1,sprintf('tau1=%2.2f',tau1)); text(2,0,sprintf('tau2=%2.2f',tau2));
text(2,1,sprintf('tau3=%2.2f',tau3)); drawnow(); %% end

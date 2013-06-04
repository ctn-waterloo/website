title: 2-link arm model

Here is matlab code that solves a simple arm model. To add forces to the arm,
you can use the keys 'q' and 'w' for the shoulder and 'o' and 'p' for the
elbow.  %%%%%%%%%%%%%%%%%%%%%%%%% %This is to run a 2D simulation of an arm in
a plane (all potential %energy is zero) % %%%%%%%%Derivation%%%%%%%% %k = 1/2
m v^2 + 1/2 I w^2 || k for rolling (translation and rotation) %I = 1/12 m
L^2pp || I of thin rod rotating about center %O1 = shoulder angle from
horizontal %O2 = relative elbow angle (from upper arm) % %Link 1 kinetic
energy %KL1 = 1/6*M1*L1^2*dO1^2; || k = 1/2*I*w^2 , I = 1/3*M*L^2 % %Link 2
kinetic energy || k = 1/2mv^2+1/2w^2 , I = 1/12ML^2 %KL2 = 1/2*m2*L1^2*dO1^2 +
1/6*m2*L2^2*(dO1^2 + dO2^2 + 2*dO1*dO2) ... % + 1/2*m2*L1*L2*cos(O2)*(dO1^2 +
dO1*dO2); % %L = KL1 + KL2; %Lagrangian w/no potential since gravity = 0 %
%Torque at link 1 %dL/dO1 = 0 %dL/ddO1 = 1/3*m2*L1^2*dO1 + 1/3*m2*L2^2*(dO1 +
dO2) ... % + 1/2*m2*L1*L2*cos(O2)*(2dO1 +dO2); %t1 = d/dt (previous) = ddO1*(
(1/3*m1+m2)*L1^2 + m2*L2*(1/3*L2 ... % + L1*cos(O2))) ... % +
ddO2*m2*L2(1/3*L2 + 1/2*L1*cos(O2)) ... % - dO2*m2*L1*L2*sin(O2)*(dO1 + dO2);
% %Torque at link 2 %dL/dO2 = -1/2*m2*L1*L2*sin(O2)*(dO1^2+dO1*dO2); %dL/ddO2
= dO1*m2*l2*(1/3*L2+1/2*L1*cos(O2)) ... % + dO2*1/3*m2*L2^2 ... % -
1/2*O1*O2*m2*L1*L2; %t2 = d/dt (previous) = ddO1*m2*l2*(1/3*L2+1/2*L1*cos(O2))
... % + ddO2*1/3*m2*L2^2 ... % + 1/2*m2*L1*L2*sin(O2)*dO1^2;
%%%%%%%%%%%%%%%%%%%%% %%Constants L1 = 1; %link 1 lengthc L2 = 1; %link 2
length m1 = 1; %link 1 mass m2 = .5; %link 2 mass dt = .01; %Simulation time
step %%Initial conditions O1t = pi/8; %Shoulder joint angle O2t = pi/8; %Elbow
joint angle dO1t = 0; %Shoulder angular velocity dO2t = 0; %Elbow angular
velocity figure(1); clf; axis([-2.5 2.5 -.2 2.5]); axis image; hold on; grid
set(gca, 'NextPlot', 'replacechildren'); set(gcf,'doublebuffer','on');
set(gcf,'KeyPressFcn','keydown=1;'); %figure(2); clf; axis image; hold on;
grid %set(gca, 'NextPlot', 'replacechildren'); %%Compute non changing
constants K1 = (1/3*m1+m2)*L1^2 + 1/3*m2*L2^2; %for ddO1 K2 = m2*L1*L2; %for
dd01 and others K3 = 1/3*m2*L2^2; %for ddO1 and ddO2 in t1 and t2 K4 =
1/2*m2*L1*L2; %for ddO1 and ddO2 %Torque equations become %t1 =
(K1+K2*cos(O2))*ddO1 + (K3+K4*cos(O2))*ddO2 ... % -
K2*(sin(O2)*dO1*dO2+1/2*sin(O2)*dO2^2); %t2 = (K3+K4*cos(O2))*ddO1 + K3*ddO2 +
1/2*K2*sin(O2)dO1^2; t = 0; tau1=0; tau2=0; ch = ''; keydown=0; mu = 0.1;
%constant of friction while (1==1) %Loop until user hits ctrl-C t = t+dt;
%tau1 = 0; %torque on shoulder %tau2 = -sin(3*t); %torque on elbow %Equations
solved for angles; mu*tau added joint friction C2 = cos(O2t); S2 = sin(O2t);
M11 = (K1 + K2*C2); M12 = (K3 + K4*C2); M21 = M12; M22 = K3; H1 =
-K2*S2*dO1t*dO2t - 1/2*K2*S2*dO2t^2; H2 = 1/2*K2*S2*dO1t^2; ddO2 = (H2*M11 -
H1*M21 - M11*tau2 + M21*tau1) / (M12^2 - M11*M22); ddO1 = (-H2 + tau2 -
M22*ddO2) / M21; %dO2 = sqrt((tau2-(K3+K4*C2)*ddO1-K3*ddO2)/(1/2*K2*S2); %dO1
= (tau1-(K1+K2*C2)*ddO1-(K3+K4*C2)*ddO2+1/2*K2*S2*dO2^2) / ... % (-K2*S2*dO2);
dO2 = dO2t+ddO2*dt; dO1 = dO1t+ddO1*dt; O1 = O1t+dO1*dt; O2 = O2t+dO2*dt;
%Enforce joint constraints if O1 <= -.1 %Shoulder too far right O1 = -.1; dO1
= 0; ddO1 = 0; elseif O1 >= pi-.2 %shoulder too far left O1 = pi-.2; dO1 = 0;
ddO1 = 0; end if O2 <= 0 %Elbow locks extended O2 = 0; dO2 = 0; ddO2 = 0;
elseif O2 >= pi-.1 %Forearm hits upper arm O2 = pi-.1; dO2 = 0; ddO2 = 0; end
%%Transfer to next time step dO1t = dO1; dO2t = dO2; O1t = O1; O2t = O2;
%%Plot arm x1 = L1*cos(O1); y1 = L1*sin(O1); %xy of elbow x2 =
x1+L2*cos(O2+O1); y2 = y1 + L2*sin(O2+O1); %xy of hand ch =
get(gcf,'CurrentCharacter'); if keydown==1 switch(ch) case 'q' %shoulder left
tau1=tau1+.1; case 'w' %shoulder right tau1 = tau1-.1; case 'o' %elbow left
tau2 = tau2+.1; case 'p' tau2 = tau2-.1; end keydown=0; end clf; hold on;
grid; axis([-2.5 2.5 -.2 2.5]); axis image; plot([0 x1],[0 y1]); %plot
shoulder to elbow plot([x1 x2],[y1,y2]) %plot elbow to hand plot(x2,y2,'ro');
%plot hand text(2,0,sprintf('tau1=%2.2f',tau1));
text(2,2,sprintf('tau2=%2.2f',tau2)); pause(.05); %drawnow; %pause; %%Plot
torque %subplot(2,1,2); hold on; axis image; %plot(t,tau1,'g+');
%plot(t,tau2,'ro'); %drawnow; end  Should be able to just paste and run this
in Matlab 7.4.

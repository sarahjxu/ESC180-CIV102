clear; close all;
%% 0. Initialize Parameters
L = 1200; % Length of bridge
n = 1200; % Discretize into 1 mm seg.
P = 400; % Total weight of train [N]
x = linspace(0, L, n+1); % x-axis
%% 1. SFD, BMD under train loading
x_train = [52 228 392 568 732 908]; % Train Load Locations
P_train = [1 1 1 1 1 1] * P/6;
n_train = 241; % num of train locations
SFDi = zeros(n_train, n+1); % 1 SFD for each train loc.
BMDi = zeros(n_train, n+1); % 1 BMD for each train loc.
% Solve for SFD and BMD with the train at different locations
for i = 1:n_train
    train_loc = linspace(0, 240, 241); % all possible start locations of train
    % sum of moments at A eqn (gives value of reaction force at B)
    B = 160 + train_loc(i)/3;
    % sum of Fy eqn (gives value of reaction force at A)
    A = 240 - train_loc(i)/3;
 
    % construct applied loads
    w = [A -P_train B]; % the amount by which the applied load changes each time
    sig_w = cumsum(w); % the new value of the applied laod after changes
    % locations of the load
    load_loc = [0 x_train+train_loc(i) 1200];
    % Matlab does not completely subtract out all the decimal places to 0,
    % so very small values will be set to 0
    smallValues = abs(sig_w) < 0.00001;
    sig_w(smallValues) = 0;
    
    % finding the number of each load/moment value required, when discretizing the load so that the diagrams have values at every mm
    load = zeros(1,8);
    for j = 1:7
        load(j) = load_loc(j+1)-load_loc(j);
    end

    % SFD = num. integral(w)
    w_discrete = repelem(sig_w, load); % repeating each value of sig_w, load number of times
    
    %% THIS WILL MAKE 241 GRAPHS OF SFD USING THE CURRENT FOR LOOP SETTINGS
    % plotting the SFD
%     figure
%     plot((1:1:1201), w_discrete, 'b', LineWidth = 2);
%     yline(0, 'k'); % x-axis line
% 
%     % drawing the vertical lines that take the SFD back to 0
%     x1 = [0 0];
%     y1 = [0 A];
%     linea = line(x1,y1);
%     linea.LineWidth = 2;
%     linea.Color = 'b';
%     x2 = [1200 1200];
%     y2 = [-B 0];
%     lineb = line(x2,y2);
%     lineb.LineWidth = 2;
%     lineb.Color = 'b';
%     title('Shear Force Diagram');
%     ylabel('Shear Force (N)');
%     xlabel('Distance of the tail of the train along bridge (mm)')

    % solving for the bending moment values
    m = cumsum(sig_w.*load);
    m_real = [0 m(1:7)]; % bending moment m, but changing the 0 point from the end to the beginning
    xq = 0:1:1200; % query points between sampling points for interpolation
    vq1 = interp1(load_loc,m_real,xq); % interpolating the values of the discretized BMD
    % making small values that should be 0 into 0, as is with the SFD
    smallValues1 = abs(vq1) < 0.00001;
    vq1(smallValues1) = 0;

    %% THIS WILL MAKE 241 GRAPHS OF BMD USING THE CURRENT FOR LOOP SETTINGS
    % plotting the BMD
%     figure
%     plot(load_loc,m_real,'ob',xq,vq1,':.b', LineWidth = 2);
%     set(gca,'YDir','reverse'); % reversing the diagram so that the positive axis points downwards
%     yline(0, 'k'); % x-axis line
%     title('Bending Moment Diagram');
%     ylabel('Bending Moment (Nmm)');
%     xlabel('Distance of the tail of the train along bridge (mm)') 
    % BMD = num. integral(SFD)

    % updating the SFDi and BMDi matrices to contain the values from this iteration
    SFDi(i, :) = [w_discrete 0];
    BMDi(i, :) = vq1;

end
SFD = max(abs(SFDi)); % SFD envelope
figure
plot(SFD)
yline(0, 'k')
BMD = max(BMDi); % BMD envelope
figure
plot(BMD)
yline(0, 'k')

%% DESIGN 0
%% 2. Define Bridge Parameters
% = xc, bt, bg, bm, bb, ht, hg, hm, hb
param = [0, 100, 1.27+5, 1.27, 80, 1.27, 1.27, 75-2*1.27, 1.27; 
    400, 100, 1.27+5, 1.27, 80, 1.27, 1.27, 75-2*1.27, 1.27;
    800, 100, 1.27+5, 1.27, 80, 1.27, 1.27, 75-2*1.27, 1.27; 
    L, 100, 1.27+5, 1.27, 80, 1.27, 1.27, 75-2*1.27, 1.27];

%x_c Location, x, of cross-section change
% Extracting user input assuming linear relationship
bt = interp1(param(:,1), param(:,2), x); % width of the top flange
bg = interp1(param(:,1), param(:,3), x); % width of the glue tabs
bm = interp1(param(:,1), param(:,4), x); % width of the webs
bb = interp1(param(:,1), param(:,5), x); % width of the base
ht = interp1(param(:,1), param(:,6), x); % height of the top flange
hg = interp1(param(:,1), param(:,7), x); % height of the glue tabs
hm = interp1(param(:,1), param(:,8), x); % height of the webs
hb = interp1(param(:,1), param(:,9), x); % height of the base


%% 3. Calculate Sectional Properties
% ybar. location of centroidal axis from the bottom

% location of the centroidal axis of each portion from the bottom
ytb = hb+hm+hg+ht./2;
ygb = hb+hm+hg./2;
ymb = hb+hm./2;
ybb = hb./2;

% area of each portion
at = ht.*bt;
ag = hg.*bg;
am = hm.*bm;
ab = hb.*bb;

ybar = (ytb.*at+2.*ygb.*ag+2.*ymb.*am+ybb.*ab)./(at+2.*ag+2.*am+ab);
ybot = ybar;
ytop = hb+hm+hb+ht-ybar;

% I
dt = abs(ytb-ybar);
dg = abs(ygb-ybar);
dm = abs(ymb-ybar);
db = abs(ybb-ybar);
I = bt.*ht.^3./12+dt.^2.*at+2.*(bg.*hg.^3./12+dg.^2.*ag)+2.*(bm.*hm.^3./12+dm.^2.*am)+bb.*hb.^3./12+db.^2.*ab;

% Q at centroidal axes
Qcent = ab.*(ybar-hb./2)+2.*bm.*(ybar-hb).*(ybar-(ybar-hb)./2-hb);

% Q at glue location
Qglue = at.*(hb+hm+hg+ht./2-ybar);

%% 4. Calculate Applied Stress
S_top = BMD.*(ytop./I);
S_bot = BMD.*(ybot./I);
T_cent = SFD.*(Qcent./(I.*2.*bm));
T_glue = SFD.*(Qglue./(I.*2.*bg));

%% 5. Material and Thin Plate Buckling Capacities
E = 4000;
mu = 0.2;
S_tens = 30;
S_comp = 6;
T_max = 4;
T_gmax = 2;
S_buck1 = (4*pi^2*E)./(12*(1-mu^2)).*(ht./(bb-bm)).^2;
S_buck2 = (0.425*pi^2*E)./(12*(1-mu^2))*(ht./((bt-bb)./2+bm./2)).^2;
S_buck3 = (6*pi^2*E)/(12*(1-mu^2)).*(bm./(ytop-ht-hg./2)).^2;
T_buck = (5*pi^2*E)/(12*(1-mu^2)).*((bm./(hm+(ht./2+hb./2))).^2+(bm./400).^2);

%% 6. FOS
FOS_tens = S_tens./S_bot;
FOS_comp = S_comp./S_top;
FOS_shear = T_max./T_cent;
FOS_glue = T_gmax./T_glue;
FOS_buck1 = S_buck1./S_top;
FOS_buck2 = S_buck2./S_top;
FOS_buck3 = S_buck3./S_top;
FOS_buckV = T_buck./T_cent;

%% 7. Min FOS and the failure load Pfail
minFOS = min([FOS_tens, FOS_comp, FOS_shear, FOS_glue, FOS_buck1, FOS_buck2, FOS_buck3, FOS_buckV]);
Pf = minFOS*400;

%% 8. Vfail and Mfail
Mf_tens = FOS_tens.*BMD;
Mf_comp = FOS_comp.*BMD;
Vf_shear = FOS_shear.*SFD;
Vf_glue = FOS_glue.*SFD;
Mf_buck1 = FOS_buck1.*BMD;
Mf_buck2 = FOS_buck2.*BMD;
Mf_buck3 = FOS_buck3.*BMD;
Vf_buckV = FOS_buckV.*SFD;

%% 9. Output plots of Vfail and Mfail
figure

subplot(2,3,1)
hold on; grid on; grid minor;
plot(x, Vf_shear, 'r')
plot(x, -Vf_shear, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Matboard Shear Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,2)
hold on; grid on; grid minor;
plot(x, Vf_glue, 'r')
plot(x, -Vf_glue, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Glue Shear Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,3)
hold on; grid on; grid minor;
plot(x, Vf_buckV, 'r')
plot(x, -Vf_buckV, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Matboard Shear Buckling Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,4)
hold on; grid on; grid minor;
plot(x, Mf_tens, 'r')
plot(x, Mf_comp, 'b')
plot(x, BMDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
set(gca,'YDir','reverse');
legend('Matboard Tension Failure', 'Matboard Compression Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,5)
hold on; grid on; grid minor;
plot(x, Mf_buck1, 'r')
plot(x, Mf_buck2, 'b')
plot(x, BMDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
set(gca,'YDir','reverse');
legend('Matboard Buckling Failure, Top Flange - Mid', 'Matboard Buckling Failure, Bottom Flange - Sides')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,6)
hold on; grid on; grid minor;
plot(x, Mf_buck3, 'r')
plot(x, -Mf_buck3, 'r')
plot(x, BMDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
set(gca,'YDir','reverse');
legend('Matboard Buckling Failure, Webs')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

%% for new cross-section 1
%% 2. Define Bridge Parameters
% = x_c, bt1, bg1, bs1, bm1, bb1, ht1, hg1, hs1, hm1, hb1
param = [0, 110, 1.27+10, 1.27, 1.27, 80, 1.27*2, 1.27, 20, 110, 1.27; 
    400, 110, 1.27+10, 1.27, 1.27, 80, 1.27*2, 1.27, 20, 110, 1.27;
    800, 110, 1.27+10, 1.27, 1.27, 80, 1.27*2, 1.27, 20, 110, 1.27; 
    L, 110, 1.27+10, 1.27, 1.27, 80, 1.27*2, 1.27, 20, 110, 1.27];

%x_c Location, x, of cross-section change
% Extracting user input assuming linear relationship
bt1 = interp1(param(:,1), param(:,2), x); % width of the top flange
bg1 = interp1(param(:,1), param(:,3), x); % width of the glue tabs
bs1 = interp1(param(:,1), param(:,4), x); % width of the diaphragm connection
bm1 = interp1(param(:,1), param(:,5), x); % width of the webs
bb1 = interp1(param(:,1), param(:,6), x); % width of the base
ht1 = interp1(param(:,1), param(:,7), x); % height of the top flange
hg1 = interp1(param(:,1), param(:,8), x); % height of the glue tabs
hs1 = interp1(param(:,1), param(:,9), x); % height of the diaphragm connection
hm1 = interp1(param(:,1), param(:,10), x); % height of the webs
hb1 = interp1(param(:,1), param(:,11), x); % height of the base

% area of each portion
at1 = ht1.*bt1;
ag1 = hg1.*bg1;
as1 = hs1.*bs1;
am1 = hm1.*bm1;
ab1 = hb1.*bb1;

% location of the centroidal axis of each portion from the bottom
yt1 = ht1./2 + hg1 + hm1 + hb1;
yg1 = hg1./2 + hm1 + hb1;
ys1 = hg1 + hm1 + hb1 - hs1./2;
ym1 = hm1./2 + hb1;
yb1 = hb1./2;

% ybar - height of the centroidal axis from the bottom
ybar1 = (at1.*yt1+2.*ag1.*yg1+as1.*ys1+2.*am1.*ym1+ab1.*yb1)./(at1+2.*ag1+as1+2.*am1+ab1);
ybot1 = ybar1;
ytop1 = hb1+hm1+hg1+ht1-ybar1;

% distance from the centroidal axis of each portion to ybar
dt1=abs(yt1-ybar1);
dg1=abs(yg1-ybar1);
ds1=abs(ys1-ybar1);
dm1=abs(ym1-ybar1);
db1=abs(yb1-ybar1);

% I
I1 = bt1.*ht1.^3./12+2.*bg1.*hg1.^3./12+bs1.*hs1.^3./12+2.*bm1.*hm1.^3./12+bb1.*hb1.^3./12+dt1.^2.*at1+2.*dg1.^2.*ag1+ds1.^2.*as1+2.*dm1.^2.*am1+db1.^2.*ab1;

% Q at centroidal axes
Qcent1 = ab1.*db1+2.*bm1.*(dm1+0.5.*hm1).*0.5.*(dm1+0.5.*hm1);

% Q at glue joint
Qglue1 = at1.*dt1;

%% 4. Calculate Applied Stress
S_top1 = BMD.*ytop1./I1;
S_bot1 = BMD.*ybot1./I1;
T_cent1 = SFD.*Qcent1./(I1.*2.*bm1);
T_glue1 = SFD.*Qglue1./(I1.*(2.*bg1+bs1));

%% 5. Material and Thin Plate Buckling Capacities
a1 = 1200/7;
S_buck11 = (4*pi^2*E)./(12*(1-mu^2)).*(ht1./(bb1-bm1)).^2;
S_buck21 = (0.425*pi^2*E)./(12*(1-mu^2)).*(ht1./((bt1-bb1)./2+bm1./2)).^2; 
S_buck31 = (6*pi^2*E)/(12*(1-mu^2)).*(bm1./(ytop1-ht1-hg1./2)).^2; 
T_buck1 = (5*pi^2*E)/(12*(1-mu^2))*((bm1./(hm1+hg1./2+hb1./2)).^2+(bm1./a1).^2);

%% 6. FOS
FOS_tens1 = S_tens./S_bot1;
FOS_comp1 = S_comp./S_top1;
FOS_shear1 = T_max./T_cent1;
FOS_glue1 = T_gmax./T_glue1;
FOS_buck11 = S_buck11./S_top1;
FOS_buck21 = S_buck21./S_top1;
FOS_buck31 = S_buck31./S_top1;
FOS_buckV1 = T_buck1./T_cent1;

%% 7. Min FOS and the failure load Pfail
minFOS1 = min([FOS_tens1, FOS_comp1, FOS_shear1, FOS_glue1, FOS_buck11, FOS_buck21, FOS_buck31, FOS_buckV1]);
Pf1 = minFOS1*400;

%% Vfail and Mfail
Mf_tens1 = FOS_tens.*BMD;
Mf_comp1 = FOS_comp.*BMD;
Vf_shear1 = FOS_shear.*SFD;
Vf_glue1 = FOS_glue.*SFD;
Mf_buck11 = FOS_buck11.*BMD;
Mf_buck21 = FOS_buck21.*BMD;
Mf_buck31 = FOS_buck31.*BMD;
Vf_buckV1 = FOS_buckV1.*SFD;

%% 9. Outputs of Vfail and Mfail
figure
subplot(2,3,1)
hold on; grid on; grid minor;
plot(x, Vf_shear1, 'r')
plot(x, -Vf_shear1, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Matboard Shear Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,2)
hold on; grid on; grid minor;
plot(x, Vf_glue1, 'r')
plot(x, -Vf_glue1, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Glue Shear Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,3)
hold on; grid on; grid minor;
plot(x, Vf_buckV1, 'r')
plot(x, -Vf_buckV1, 'r')
plot(x, SFDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
legend('Matboard Shear Buckling Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,4)
hold on; grid on; grid minor;
plot(x, Mf_tens1, 'r')
plot(x, Mf_comp1, 'b')
plot(x, BMDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
set(gca,'YDir','reverse');
legend('Matboard Tension Failure', 'Matboard Compression Failure')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,5)
hold on; grid on; grid minor;
plot(x, Mf_buck11, 'r')
plot(x, Mf_buck21, 'b')
plot(x, BMDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
set(gca,'YDir','reverse');
legend('Matboard Buckling Failure, Top Flange - Mid', 'Matboard Buckling Failure, Bottom Flange - Sides')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

subplot(2,3,6)
hold on; grid on; grid minor;
plot(x, Mf_buck31, 'r')
plot(x, -Mf_buck31, 'r')
plot(x, BMDi, 'k');
plot([0, L], [0, 0], 'k', 'LineWidth', 2)
set(gca,'YDir','reverse');
legend('Matboard Buckling Failure, Webs')
xlabel('Distance along bridge (mm)')
ylabel('Shear Force (N)')

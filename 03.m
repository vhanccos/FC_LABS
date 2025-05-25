clear, clf, hold off; n=0; h=0.01;
k=1; m=2;
t=0; tfin = 2;
vx = 2; vy = 8;
x = 0; y = 0;
pvx(1)=vx; pvy(1)=vy; px(1)=x; py(1)=y;
ax = 0;
ay = -10;
for t=0:h:tfin
    n=n+1;
    vx = vx + h*ax;
    vy = vy + h*ay;
    x = x + vx*h;
    y = y + vy*h;
    px(n+1)=x;
    py(n+1)=y;
end
subplot(2,2,1), plot(px,py); grid on;

clear, clf, hold off; n=0; h=0.01;
% Constantes del Sistema
k=1; m=2;
% Condiciones Iniciales
t=0; tfin = 2;
vx = 2.5; vy = 2.5*sqrt(3);
x = 0; y = 0;
% Inicio de la Simulacion
pvx(1)=vx; pvy(1)=vy; px(1)=x; py(1)=y;
ax = 0; % consideramos una aceleracion constante para x
ay = -10; % consideramos una aceleracion de - 10 para y para simular gravedad
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

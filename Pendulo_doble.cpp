#include <iostream>
#include <cmath>
#include <fstream>
#include <algorithm>

using namespace std;
#define g 9.80665
#define pi 3.141592
#define h 0.02
#define tf 40

double fipuntof(double pfi, double ppsi, double fi, double psi);
double psipuntof(double pfi, double ppsi, double fi, double psi);
double pfipunto(double pfi, double ppsi, double fi, double psi);
double ppsipunto(double pfi, double ppsi, double fi, double psi);

int main(void)
{   
    bool cambio;
    double psi, psipunto, ppsi, fi, fipunto, pfi, E, k[4][4],t,aux,aux2;
    int i,j, contador;
    ofstream pos;
    ofstream poincareppsi;
    ofstream poincarepsi;
    ofstream pospoincare;
    ofstream poincarepfi;
    ofstream poinpfit;
    ofstream poinppsit;
    ofstream poincare;

    //Ahora inicializamos los parametro

    contador=0;
    E=25.;
    psi=0.2; //E=15-> pi/3    E=10-> pi/4     E=5-> pi/6      E=3-> pi/7     E=1-> pi/13
    fi=0.2;
    aux=0.;
    aux2=0.0;

    psipunto=0.0;                                               //1
    fipunto=sqrt(E-2.*g*(1-cos(fi))-g*(1-cos(psi)));            //1
    //fipunto=0.0;                                              //2
    //psipunto=sqrt(2.*(E-2.*g*(1-cos(fi))-g*(1-cos(psi))));    //2
    
    ppsi=fipunto*cos(psi-fi)+psipunto;
    pfi=2*fipunto+psipunto*cos(psi-fi);  

    pos.open("0_2.dat");
    poincareppsi.open("poincareppsi.dat");
    poincarepsi.open("poincarepsi.dat");
    pospoincare.open("pospoincare.dat");
    poincarepfi.open("poincarepfi.dat");
    poinpfit.open("pfit.dat");
    poinppsit.open("ppsit_2.dat");
    poincare.open("fase0_2.dat");

    for ( t = 0; t < tf; t=t+h)
    {   
        if (psipuntof(pfi,ppsi,fi,psi)*aux<0)                                           //Superficie de Poincaré
        {
            poincarepsi << psi << "     " << fi << endl;
            poincareppsi << psi << "    " << psipuntof(pfi,ppsi,fi,psi) << endl;
            poincarepfi << psi << "     " << fipuntof(pfi,ppsi,fi,psi) << endl;
        }
                /*if (fipuntof(pfi,ppsi,fi,psi)*aux2<0)                                 //Otra Superficie de Poincaré
        {
            poincarepsi << psi << "     " << fi << endl;
            poincareppsi << psi << "    " << psipuntof(pfi,ppsi,fi,psi) << endl;
            poincarepfi << psi << "     " << fipuntof(pfi,ppsi,fi,psi) << endl;
        }*/

        poincare << psi << ",     " << fi << endl;                                      //Trayectoria de espacio de fase
        poinpfit << psi << ",     " << fipuntof(pfi,ppsi,fi,psi) << endl;
        poinppsit << psi << ",    " << psipuntof(pfi,ppsi,fi,psi) << endl;

        
        
        pos << sin(fi) << ",     " << -cos(fi) << endl << sin(fi)+sin(psi) << ",    " << -cos(fi)-cos(psi) << endl << endl;        //Posición péndulo para simulación

        //Evaluamos los k donde el primer indice indica el superindice de k y el segundo indica de que coordenada
        //El primero es fi, psi, pfi, ppsi

        aux=psipuntof(pfi,ppsi,fi,psi);
        aux2=fipuntof(pfi,ppsi,fi,psi);

        k[0][0]=h*fipuntof(pfi,ppsi,fi,psi);
        k[0][1]=h*psipuntof(pfi,ppsi,fi,psi);
        k[0][2]=h*pfipunto(pfi,ppsi,fi,psi);
        k[0][3]=h*ppsipunto(pfi,ppsi,fi,psi);

        k[1][0]=h*fipuntof(pfi+k[0][2]/2.0,ppsi+k[0][3]/2.0,fi+k[0][0]/2.0,psi+k[0][1]/2.0);
        k[1][1]=h*psipuntof(pfi+k[0][2]/2.0,ppsi+k[0][3]/2.0,fi+k[0][0]/2.0,psi+k[0][1]/2.0);
        k[1][2]=h*pfipunto(pfi+k[0][2]/2.0,ppsi+k[0][3]/2.0,fi+k[0][0]/2.0,psi+k[0][1]/2.0);
        k[1][3]=h*ppsipunto(pfi+k[0][2]/2.0,ppsi+k[0][3]/2.0,fi+k[0][0]/2.0,psi+k[0][1]/2.0);

        k[2][0]=h*fipuntof(pfi+k[1][2]/2.0,ppsi+k[1][3]/2.0,fi+k[1][0]/2.0,psi+k[1][1]/2.0);
        k[2][1]=h*psipuntof(pfi+k[1][2]/2.0,ppsi+k[1][3]/2.0,fi+k[1][0]/2.0,psi+k[1][1]/2.0);
        k[2][2]=h*pfipunto(pfi+k[1][2]/2.0,ppsi+k[1][3]/2.0,fi+k[1][0]/2.0,psi+k[1][1]/2.0);
        k[2][3]=h*ppsipunto(pfi+k[1][2]/2.0,ppsi+k[1][3]/2.0,fi+k[1][0]/2.0,psi+k[1][1]/2.0);

        k[3][0]=h*fipuntof(pfi+k[2][2],ppsi+k[2][3],fi+k[2][0],psi+k[2][1]);
        k[3][1]=h*psipuntof(pfi+k[2][2],ppsi+k[2][3],fi+k[2][0],psi+k[2][1]);
        k[3][2]=h*pfipunto(pfi+k[2][2],ppsi+k[2][3],fi+k[2][0],psi+k[2][1]);
        k[3][3]=h*ppsipunto(pfi+k[2][2],ppsi+k[2][3],fi+k[2][0],psi+k[2][1]);

        fi=fi+(k[0][0]+2.0*k[1][0]+2.0*k[2][0]+k[3][0])/6.0;
        psi=psi+(k[0][1]+2.0*k[1][1]+2.0*k[2][1]+k[3][1])/6.0;
        pfi=pfi+(k[0][2]+2.0*k[1][2]+2.0*k[2][2]+k[3][2])/6.0;
        ppsi=ppsi+(k[0][3]+2.0*k[1][3]+2.0*k[2][3]+k[3][3])/6.0;

        contador=contador+1;
    }

    return 0;
}

double fipuntof(double pfi, double ppsi, double fi, double psi)
{
    double fipunto;

    fipunto=(pfi-(ppsi)*cos(psi-fi))/(2.-pow(cos(psi-fi),2));

    return fipunto;
}

double psipuntof(double pfi, double ppsi, double fi, double psi)
{
    double psipunto;

    psipunto=(2.*ppsi-cos(psi-fi)*pfi)/(2.-pow(cos(psi-fi),2));

    return psipunto;
}

double pfipunto(double pfi, double ppsi, double fi, double psi)
{
    double pfipunto,auxiliar,auxiliar2;

    auxiliar=pfi*ppsi*sin(fi-psi)/(1.0+pow(sin(fi-psi),2));
    auxiliar2=(pfi*pfi+2.0*ppsi*ppsi-2.0*pfi*ppsi*cos(fi-psi))/(2*pow(1.0+pow(sin(fi-psi),2),2));
    pfipunto=-2.0*g*sin(fi)-auxiliar+auxiliar2*sin(2*(fi-psi));

    return pfipunto;
}

double ppsipunto(double pfi, double ppsi, double fi, double psi)
{
    double ppsipunto,auxiliar,auxiliar2;

    auxiliar=pfi*ppsi*sin(fi-psi)/(1.0+pow(sin(fi-psi),2));
    auxiliar2=(pfi*pfi+2.0*ppsi*ppsi-2.0*pfi*ppsi*cos(fi-psi))/(2*pow(1.0+pow(sin(fi-psi),2),2));
    ppsipunto=-1.0*g*sin(psi)+auxiliar-auxiliar2*sin(2*(fi-psi));

    return ppsipunto;
}

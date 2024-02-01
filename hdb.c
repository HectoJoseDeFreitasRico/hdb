#include <stdio.h>

int main(){
	FILE *archivo;
	archivo = fopen("basededatos.txt","w");
	char *texto = "HDB";
	fputs(texto,archivo);
	fclose(archivo);
	return 0;
}
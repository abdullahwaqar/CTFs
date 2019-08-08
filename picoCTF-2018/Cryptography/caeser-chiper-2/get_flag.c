#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	char *str = "d]Wc7H:oW5YgUFS7]D'\'9fGS^iGHSUF9bHSg9WIf9q";   //CipherText
	int len;
	len=strlen(str);											//CipherText Length
	int i,j;
	
	for(i=33;i<127;i++)
	{
		printf("%d\t",i);
		for(j=0;j<len;j++)
		{
			if((str[j]+i) > 127)							//If the shift of number goes out of ascii range
			printf("%c",33+(str[j]+i)-127);					
			else
			printf("%c",(str[j]+i));
			
		}
		printf("\n");
	}
	
	
	return 0;
}
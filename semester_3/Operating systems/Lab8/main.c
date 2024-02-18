#include <windows.h>
#include <process.h>
#include <stdio.h>
#include <time.h>

HANDLE hthread[5],hsm,hsm1;
char   buffer[12],buff[12];
void GoToXY(const int X,const int Y){//аналог встроенной функции gotoxy. Взята данная функция т.к gotoxy не поддерживалась 
                                      //моим компилятором//код функции взят с интернета
    HANDLE OutputHandle;
    CONSOLE_SCREEN_BUFFER_INFO ScreenBufInfo;
    OutputHandle=GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleScreenBufferInfo(OutputHandle,&ScreenBufInfo);
    ScreenBufInfo.dwCursorPosition.X=X;
    ScreenBufInfo.dwCursorPosition.Y=Y;
    SetConsoleCursorPosition(OutputHandle,ScreenBufInfo.dwCursorPosition);
}
DWORD WINAPI Writer(void*n){//функция писатель, используемая как прототип для создания нитей-писателей
 short i;
 while(1) {
WaitForSingleObject(hsm,3000);//ожидание освобождения семафора, максимальное время ожидания 3 сек.
if((int)n==3){//определение того, что нужно записать в буфер
	strncpy(buff,"Novosibirsk", 12);//заполнение массива, откуда будут браться данные в буфер
}else if((int)n==4){
	strncpy(buff,"Ekaterinburg", 12);
}else if((int)n==5){
	strncpy(buff,"Semipalatink", 12);
}
    for(i=0;i<=5;i++){//запись первой половины в буфер
    	buffer[i] = buff[i];
    }
    Sleep(1000);//пауза 1 сек.
    for(i=6;i<=11;i++){//запись второй половины в буфер
    	buffer[i]=buff[i];
    }
    ReleaseSemaphore(hsm1,1,NULL);//освобождение семафора
   }
   return 0;
}
DWORD WINAPI Reader(void*n){//функция читатель, используемая как прототип для создания нитей-читателей
 short i=0,j;
 while(1){
    i++;//для смещения позиции вниз на 1 строку
WaitForSingleObject(hsm1,INFINITE);//ожидание освобождения семафора
      GoToXY(((int)n+1)*20,i);//задается позиция вывода
      printf("%s",buffer);//непосредственно вывод
      ReleaseSemaphore(hsm,1,NULL);//освобождение семафора
      Sleep(290);//пауза
    }
 return(0);
}

void main(){
 int i;
 system("cls");//очистка экрана
 hsm = CreateSemaphore(NULL,0,1,NULL);//создание семафора
 hsm1 = CreateSemaphore(NULL,0,1,NULL);
 for (i=3;i<=5;i++){     //создание писателей
     hthread[i]=CreateThread(NULL,4096,Writer,(void*)i,0,NULL);
 }
 for (i=0;i<=2;i++){//создание читателей
     hthread[i]=CreateThread(NULL,4096,Reader,(void*)i,0,NULL);
 }
ReleaseSemaphore(hsm,1,NULL);//освобождение семафора
 getchar();//ожидаем ввод для закрытия программы
 for (i=0;i<=4;i++)CloseHandle(hthread[i]);//закрываем все потоки
 CloseHandle(hsm);
}

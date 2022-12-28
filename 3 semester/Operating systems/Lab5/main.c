#include <windows.h>
#include <stdio.h>

void main() {
	char* buffer, symbol;
	DWORD symlen, actlen = 0;
	HANDLE fhandl, hstdin, hstdout;
	fhandl = CreateFile("text.txt", GENERIC_READ, FILE_SHARE_READ, 0, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0);
	if (fhandl == INVALID_HANDLE_VALUE) {
		return;
	}
	DWORD size = GetFileSize(fhandl, NULL);
	buffer = (char*)malloc(size * sizeof(char));
	
	hstdin = GetStdHandle(STD_INPUT_HANDLE);
	if (hstdin == INVALID_HANDLE_VALUE)
		return;
	hstdout = GetStdHandle(STD_OUTPUT_HANDLE);
	if (hstdout == INVALID_HANDLE_VALUE)
		return;

	INPUT_RECORD ibuf;
	COORD symbolC;
	ibuf.EventType = MOUSE_EVENT;

	ReadFile(fhandl, buffer, size, &actlen, NULL);
	WriteFile(hstdout, buffer, size, &actlen, NULL);

	SetConsoleMode(hstdin, ENABLE_EXTENDED_FLAGS | ENABLE_MOUSE_INPUT);
	
	printf("\n");
	while (1) {
		if (ReadConsoleInput(hstdin, &ibuf, 1, &symlen)) {

			if (ibuf.Event.MouseEvent.dwButtonState == RIGHTMOST_BUTTON_PRESSED) {
				return;
			}
			
			if (ibuf.Event.MouseEvent.dwButtonState == FROM_LEFT_1ST_BUTTON_PRESSED) {
				symbolC.X = ibuf.Event.MouseEvent.dwMousePosition.X;
				symbolC.Y = ibuf.Event.MouseEvent.dwMousePosition.Y;
				ReadConsoleOutputCharacter(hstdout, &symbol, 1, symbolC, &symlen);

				if (symbol != ' ') {
					printf("%c (%d, %d)", symbol, symbolC.X, symbolC.Y);
				}
			}
		}
	}
}

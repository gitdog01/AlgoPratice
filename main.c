#include <stdio.h>
#include <stdlib.h>

int main() {
   int C;            //케이스 수
   scanf("%d", &C);

   int N;            //학생 수
   int i, j;         //반복문에 사용 할 지수
   double avg = 0.0;   //각 케이스마다 초기화
   int sum = 0;      //각 케이스마다 초기화
   int count = 0;      //평균 넘는 학생수 카운트
                  //출력에 사용할 각 케이스 별 결과 동적할당
   double *result = (double *)malloc(C * sizeof(double));

   //입력받아 결과 도출
   for (i = 0; i < C; i++) {    //케이스 수 만큼 반복
      scanf("%d", &N);
      int *score = (int *)malloc(N * sizeof(int));
      j = 0;
      while (scanf("%d", &score[j]) != EOF) {
         sum += score[j];
         j++;
      }
      /*
      for (j = 0; j < N; j++) {    //각 케이스 별 학생 수 만큼 반복
         scanf("%d", &score[j]);
         sum += score[j];
      }
      */
      avg = (double)sum / (double)N;
      for (j = 0; j < N; j++) {    //각 케이스 별 학생 수 만큼 반복
         if (score[j] > avg) {
            count++;
         }
      }
      result[i] = (double)count / (double)N * 100.0;

      //결과 도출에 재사용 할 변수들 초기화
      //케이스 별 점수 또한 따로 저장해 두지 않음(free 사용)
      avg = 0.0;
      sum = 0;
      count = 0;
      free(score);
   }

   //결과 출력
   for (i = 0; i < C; i++) {
      printf("%.3lf\n", result[i]);
   }

   return 0;
}
#include <stdio.h>
#include <stdlib.h>

int main() {
   int C;            //���̽� ��
   scanf("%d", &C);

   int N;            //�л� ��
   int i, j;         //�ݺ����� ��� �� ����
   double avg = 0.0;   //�� ���̽����� �ʱ�ȭ
   int sum = 0;      //�� ���̽����� �ʱ�ȭ
   int count = 0;      //��� �Ѵ� �л��� ī��Ʈ
                  //��¿� ����� �� ���̽� �� ��� �����Ҵ�
   double *result = (double *)malloc(C * sizeof(double));

   //�Է¹޾� ��� ����
   for (i = 0; i < C; i++) {    //���̽� �� ��ŭ �ݺ�
      scanf("%d", &N);
      int *score = (int *)malloc(N * sizeof(int));
      j = 0;
      while (scanf("%d", &score[j]) != EOF) {
         sum += score[j];
         j++;
      }
      /*
      for (j = 0; j < N; j++) {    //�� ���̽� �� �л� �� ��ŭ �ݺ�
         scanf("%d", &score[j]);
         sum += score[j];
      }
      */
      avg = (double)sum / (double)N;
      for (j = 0; j < N; j++) {    //�� ���̽� �� �л� �� ��ŭ �ݺ�
         if (score[j] > avg) {
            count++;
         }
      }
      result[i] = (double)count / (double)N * 100.0;

      //��� ���⿡ ���� �� ������ �ʱ�ȭ
      //���̽� �� ���� ���� ���� ������ ���� ����(free ���)
      avg = 0.0;
      sum = 0;
      count = 0;
      free(score);
   }

   //��� ���
   for (i = 0; i < C; i++) {
      printf("%.3lf\n", result[i]);
   }

   return 0;
}
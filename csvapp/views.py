from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from io import StringIO
from .models import MyData
from .serializers import MyDataSerializer

class UploadCSVView(APIView):
    def post(self, request, format=None):
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(StringIO(decoded_file))
        next(csv_data)
        for row in csv_data:
            my_data = MyData(emp_num=row[0], emp_name=row[1])
            my_data.save()

        return Response({'message': 'CSV file parsed and data inserted successfully.'})

class Top50RowsView(APIView):
    def get(self, request, format=None):
        sort_column = request.query_params.get('column_name', 'emp_num')
        sort_order = request.query_params.get('sort_order', 'asc')
        count = request.query_params.get('count','50')
        if sort_order == 'desc':
            queryset = MyData.objects.all().order_by('-' + sort_column)[:int(count)]
        else:
            queryset = MyData.objects.all().order_by(sort_column)[:int(count)]

        serializer = MyDataSerializer(queryset, many=True)
        return Response(serializer.data)
import re

def main():
    car_numbers = ["А123АА11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12", "Е145ТС96", "Н653ОЕ81", "РН12О45","РР543750"]
    pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}(01|02|102|03|04|05|06|07|08|09|10|11|12|13|113|14|15|16|116|716|17|18|19|21|121|22|23|93|123|24|84|88|124|25|125|26|126|27|28|29|30|31|32|33|34|134|35|36|136|37|38|85|138|39|91|40|41|42|142|43|44|45|46|47|147|48|49|50|90|150|190|750|51|52|152|53|54|154|55|56|156|57|58|59|81|159|60|61|161|761|62|63|163|763|64|164|65|66|96|196|67|68|69|70|71|72|73|173|74|174|75|80|76|77|97|99|177|197|199|777|799|78|98|178|198|79|82|83|86|186|87|89|92|94|95)'
    right_numbers = []

    for number in car_numbers:
        if(re.match(pattern, number)):
            right_numbers.append(number)


    print(right_numbers)

if __name__ == '__main__':
    main()

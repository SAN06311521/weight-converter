pounds = 0
kilograms = 0.0
ounces = 0.0
stones = 0.0
metric_tonnes = 0.0
troy_pounds = 0.0
grams = 0.0
milligrams = 0.0
micrograms = 0.0
restart='y'
while restart == 'y'or restart == "Y":
    
    print("Choose any Quantity:")
    print("1.Pounds\n2.Kilograms\n3.Ounces\n4.Stones\n5.Metric Tonnes\n6.Troy Pounds\n7.Grams\n8.Milligrams\n9.Micrograms")
    weight_type = str(input())
    input_weight = float(input("Enter The Value:"))
    if weight_type == '1':
        pounds = input_weight
        kilograms = input_weight*0.453
        ounces = input_weight*16
        stones = input_weight*0.0714
        metric_tonnes = input_weight*4.538*10**-4
        troy_pounds = input_weight*1.2153
        grams = input_weight*453.59
        milligrams = input_weight*453592
        micrograms = input_weight*4.536*10**8
    elif weight_type == '2':
        pounds = input_weight*2.2046
        kilograms = input_weight
        ounces = input_weight*35.274
        stones = input_weight*0.15747
        metric_tonnes = input_weight*0.001
        troy_pounds = input_weight*2.6792
        grams = input_weight*1000
        milligrams = input_weight*1000000
        micrograms = input_weight*10**9
    elif weight_type == '3':
        pounds = input_weight*0.0625
        kilograms = input_weight*0.02835
        ounces = input_weight
        stones = input_weight*0.0044643
        metric_tonnes = input_weight*2.835*10**-5
        troy_pounds = input_weight*0.075955
        grams = input_weight*28.35
        milligrams = input_weight*28350
        micrograms = input_weight*2.835*10**7
    elif weight_type == '4':
        pounds = input_weight*14
        kilograms = input_weight*6.3503
        ounces = input_weight*224.0
        stones = input_weight
        metric_tonnes = input_weight*0.0063503
        troy_pounds = input_weight*17.014
        grams = input_weight*6350.3
        milligrams = input_weight*6350293
        micrograms = input_weight*6.35*10**9
    elif weight_type == '5':
        pounds = input_weight*2204.6
        kilograms = input_weight*1000
        ounces = input_weight*35274
        stones = input_weight*157.47
        metric_tonnes = input_weight
        troy_pounds = input_weight*2679.2
        grams = input_weight*1000000
        milligrams = input_weight*1*10**9
        micrograms = input_weight*1*10**12
    elif weight_type == '6':
        pounds = input_weight*0.82286
        kilograms = input_weight*0.37324
        ounces = input_weight*13.166
        stones = input_weight*0.058776
        metric_tonnes = input_weight*3.7324*10**-4
        troy_pounds = input_weight
        grams = input_weight*5760
        milligrams = input_weight*373242
        micrograms = input_weight*3.732*10**8
    elif weight_type == '7':
        pounds = input_weight*0.0022046
        kilograms = input_weight*0.001
        ounces = input_weight*0.35274
        stones = input_weight*1.5747*10**-4
        metric_tonnes = input_weight*1*10**-6
        troy_pounds = input_weight*0.0026792
        grams = input_weight
        milligrams = input_weight*1000
        micrograms = input_weight*1*10**6
    elif weight_type == '8':
        pounds = input_weight*2.2046*10**-6
        kilograms = input_weight*1*10**-6
        ounces = input_weight*3.5274*10**-5
        stones = input_weight*1.5747*10**-7
        metric_tonnes = input_weight*1*10**-9
        troy_pounds = input_weight*2.6792*10**-6
        grams = input_weight*0.001
        milligrams = input_weight
        micrograms = input_weight*1000
    elif weight_type == '9':
        pounds = input_weight*2.205*10**-9
        kilograms = input_weight*10**-9
        ounces = input_weight*3.527*10**-8
        stones = input_weight*1.575*10**-10
        metric_tonnes = input_weight*10**-12
        troy_pounds = input_weight*2.679*10**-9
        grams = input_weight*10**-6
        milligrams = input_weight*10**-6
        micrograms = input_weight
    else:
         print("Invalid Option")
    print("\n\n\nPounds="+str(pounds)+"\nKilograms="+str(kilograms)+"\nOunces="+str(ounces)+"\nStones="+str(stones)+"\nMetric Tonnes="+str(metric_tonnes)+"\nTroy Pounds="+str(troy_pounds)+"\nGrams="+str(grams)+"\nMilligrams="+str(milligrams)+"\nMicrograms="+str(micrograms))
    restart=input("Press Y to continue ,N to exit")

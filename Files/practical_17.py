'''
Name:- Kamaltosh Jha
Section A Group 1
Title :- Write a menu driven Program to determine different characteristics using various Queuing models

'''
#****************Program******************
import math

def mm1(lambd, mu):
    rho = lambd / mu
    if rho < 1:
        lq = rho**2 / (1 - rho)
        wq = lq / lambd
        l = rho / (1 - rho)
        w = wq + (1 / mu)
        p0 = 1 - rho
    else:
        print("Invalid! Utilization factor should be less than 1 for M/M/c model.")
        lq, wq, l, w, p0= None, None, None, None, None
    return lq, wq, l, w, p0

def mmc(lambd, mu, c):
    rho = lambd / (c * mu)
    r = lambd/mu

    if rho < 1:
        summation1 = 0
        for i in range(c):
            summation1 += (r**i)/math.factorial(i)
        summation2 = (r**c)/(math.factorial(c)*(1-rho))

        p0 = 1/(summation1 + summation2)
        lq = (rho * (r ** c) * p0 )/ (math.factorial(c) * (1 - rho))
        l = lq + r
        w = l / lambd
        wq = lq/lambd
    else:
        print("Invalid! Utilization factor should be less than 1 for M/M/c model.")
        lq, wq, l, w, p0 = None, None, None, None, None
    return lq, wq, l, w, p0

def mm1k(lambd, mu, K):
    rho = lambd / mu
    if (rho == 1):
        p0 = 1/(1+K)
        l = K/2
        lq =( K*(K-1))/(2*(K+1))

    else:
        p0 = (1-rho)/(1-rho**(K+1))
        l = (rho * (K * (rho ** (K+1)) - (K+1) * (rho**K) + 1))/((1-rho)*(1-(rho ** (K+1))))
        lq = l - rho
    pk = (rho**K)*p0
    lambd_eff = lambd/(1-pk)
    w = l/lambd_eff
    wq = lq/lambd_eff
    return lq, wq, l, w, pk, p0

repeat = 1
while repeat:
    print("Queuing Model Characteristics Calculator")
    print("1. M/M/1 Model")
    print("2. M/M/c Model")
    print("3. M/M/1/K Model")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        lambd = float(input("Enter average arrival rate (lambda): "))
        mu = float(input("Enter average service rate (mu): "))
        lq, wq, l, w, p0= mm1(lambd, mu)
        if lq is not None:
            print(f"Probability of zero customers in the system: {p0}")
            print(f"Average number in queue (Lq): {lq}")
            print(f"Average time in queue (Wq): {wq}")
            print(f"Average number in the system (l): {l}")
            print(f"Average time in the system (W): {w}")

    elif choice == 2:
        lambd = float(input("Enter average arrival rate (lambda): "))
        mu = float(input("Enter average service rate (mu): "))
        c = int(input("Enter number of servers (c): "))
        lq, wq, l, w, p0 = mmc(lambd, mu, c)
        if lq is not None:
            print(f"Probability of zero customers in the system: {p0}")
            print(f"Average number in queue (Lq): {lq}")
            print(f"Average time in queue (Wq): {wq}")
            print(f"Average number in the system (l): {l}")
            print(f"Average time in the system (W): {w}")

    elif choice == 3:
        lambd = float(input("Enter average arrival rate (lambda): "))
        mu = float(input("Enter average service rate (mu): "))
        K = float(input("Enter System Size "))
        lq, wq, l, w, pk, p0= mm1k(lambd, mu, K)
        print(f"Probability of zero customers in the system: {p0}")
        print(f"Probability of K customers in the system: {pk}")
        print(f"Average number in queue (Lq): {lq}")
        print(f"Average time in queue (Wq): {wq}")
        print(f"Average number in the system (l): {l}")
        print(f"Average time in the system (W): {w}")

    else:
        print("Invalid choice. Please enter a valid option.")
    
    repeat = int(input("Do you want to calculate another model? Enter 1 for yes and 0 for no "))

'''
#********OUTPUT********
Queuing Model Characteristics Calculator
1. M/M/1 Model
2. M/M/c Model
3. M/M/1/K Model
Enter your choice (1-3): 1
Enter average arrival rate (lambda): 5
Enter average service rate (mu): 10
Probability of zero customers in the system: 0.5
Average number in queue (Lq): 0.5
Average time in queue (Wq): 0.1
Average number in the system (l): 1.0
Average time in the system (W): 0.2
Do you want to calculate another model? Enter 1 for yes and 0 for no 1
Queuing Model Characteristics Calculator
1. M/M/1 Model
2. M/M/c Model
3. M/M/1/K Model


Enter your choice (1-3): 2
Enter average arrival rate (lambda): 5
Enter average service rate (mu): 10
Enter number of servers (c): 1
Probability of zero customers in the system: 0.5
Average number in queue (Lq): 0.25
Average time in queue (Wq): 0.05
Average number in the system (l): 0.75
Average time in the system (W): 0.15
Do you want to calculate another model? Enter 1 for yes and 0 for no 1
Queuing Model Characteristics Calculator
1. M/M/1 Model
2. M/M/c Model
3. M/M/1/K Model


Enter your choice (1-3): 3
Enter average arrival rate (lambda): 5
Enter average service rate (mu): 10
Enter System Size 9999999 
Probability of zero customers in the system: 0.5
Probability of K customers in the system: 0.0
Average number in queue (Lq): 0.5
Average time in queue (Wq): 0.1
Average number in the system (l): 1.0
Average time in the system (W): 0.2
Do you want to calculate another model? Enter 1 for yes and 0 for no 0
'''
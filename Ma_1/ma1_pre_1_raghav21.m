%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Course Number: ENGR 13300
% Semester: Fall 2024
%
% Problem Description: Assign values and use trig functions. Also assign
% and use matrix functions
%
% Assignment Information
%   Assignment:     12.1.2 - MA1
%   Author:         Ankur Raghavan, raghav21@purdue.edu
%   Team ID:        022-11
%   Date:           10/18/2024
%
%   Contributor:    Name, login@purdue [repeat for each]
%   My contributor(s) helped me:
%     [ ] understand the assignment expectations without
%         telling me how they will approach it.
%     [ ] understand different ways to think about a solution
%         without helping me plan my solution.
%     [ ] think through the meaning of a specific error or
%         bug present in my code without looking at my code.
%   Note that if you helped somebody else with their code, you
%   have to list that person as a contributor here as well.
%
% Academic Integrity Statement:
%     I have not used source code obtained from any unauthorized
%     source, either modified or unmodified; nor have I provided
%     another student access to my code.  The project I am
%     submitting is my own original work.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% ____________________
%% INITIALIZATION
%a=input("Enter a:");
%b=input("Enter b:");
%c=input("Enter c:");
a=5;
b=1;
c=2;
%% ____________________
%% CALCULATIONS
d= a*(b^4)+tan(c);
e= (pi/c)-factorial(b)+a/15;
f= b^5+c/4+asin(1);
%% ____________________
%% OUTPUTS
fprintf("The result to the first calculation is %.3f\n",d);
fprintf("The result to the second calculation is %.3f\n",e);
fprintf("The result to the third calculation is %.3f\n",f);

%% ____________________
%% VECTOR/MATRIX INITIALIZATION
v1 = [1, 17, 4];
m1 = [4, 6, 19; 3, 52, 6; 7, 9, 14];

%% ____________________
%% VECTOR/MATRIX CALCULATION
v1(2)=8
m1(1,1)=v1(1);
m1(1,2)=v1(2);
m1(1,3)=v1(3)

# Number Summer

A command-line Python program that accumulates user input numbers in a running total until the sum reaches 1000 or more. This project demonstrates loop control, input handling, and running calculations.

## 🎯 About This Project

This project explores fundamental programming concepts:
- **Loop control** - Understanding when to continue and when to stop iterating
- **Accumulation pattern** - Building running totals from sequential inputs
- **Conditional exit** - Using conditions to determine loop termination
- **Real-time calculation** - Updating values as new input arrives

The program implements a common pattern in programming where you need to collect data until a specific condition is met, then process and display the result.

## ✨ Features

- ✅ **Continuous Input Loop** - Accepts multiple numbers from user
- ✅ **Running Total** - Tracks accumulated sum in real-time
- ✅ **Smart Termination** - Stops when sum reaches 1000 or more
- ✅ **Final Output** - Displays the complete sum when loop ends
- ✅ **Simple Interface** - Easy-to-use command-line interface
- ✅ **Quick Feedback** - Responds to each number immediately

## 📋 Requirements

- **Python 3.6+** - Uses standard Python features
- **No external dependencies** - Uses only built-in Python functions

## 🚀 Installation & Usage

### Clone the Repository


git clone [https://github.com/Miami05/number-summer.git](https://github.com/Miami05/number-summer.git)  

```bash
cd number-summer
```


### Run the Program
```bash
python3 main.py
```


### Example Usage

**Example 1: Reaching 1000 with various inputs**
Enter a number: 400  
Enter a number: 400  
Enter a number: 300  
Final sum: 1100

**Example 2: Exceeding 1000**

Enter a number: 400  
Enter a number: 400  
Enter a number: 300  
Final sum: 1100

**Example 3: Single large number**
Enter a number: 1500  
Final sum: 1500


**Example 4: Many small numbers**
Enter a number: 1  
Enter a number: 2  
Enter a number: 3  
Enter a number: 4  
Enter a number: 5  
Enter a number: 100  
Enter a number: 200  
Enter a number: 300  
Enter a number: 400  
Final sum: 1015


## 📝 Code Structure

### Main Function

**`main()`**
- **Purpose:** Entry point for the program
- **Logic:**
  1. Initialize `total` to 0
  2. Loop while `total < 1000`
  3. Get user input as integer
  4. Add input to running total
  5. Exit loop when total reaches 1000 or more
  6. Display final sum

### How It Works

Step 1: Start with total = 0  
Is 0 < 1000? Yes → Enter loop

Step 2: Ask user for number → Input: 200  
total = 0 + 200 = 200  
Is 200 < 1000? Yes → Continue loop

Step 3: Ask user for number → Input: 300  
total = 200 + 300 = 500  
Is 500 < 1000? Yes → Continue loop

Step 4: Ask user for number → Input: 250  
total = 500 + 250 = 750  
Is 750 < 1000? Yes → Continue loop

Step 5: Ask user for number → Input: 300  
total = 750 + 300 = 1050  
Is 1050 < 1000? No → Exit loop

Step 6: Print "Final sum: 1050


## 🔍 Loop Mechanics

The core of this program is the **while loop with accumulation pattern**:

total = 0 # Initialize accumulator  
while total < 1000: # Condition: continue until threshold  
num = int(input(...)) # Get new value  
total += num # Add to running total  
print(f"Final sum: {total}") # Output result


### Key Points

- **Pre-loop initialization** - Must set `total = 0` before the loop
- **Condition check** - Happens before each iteration
- **Accumulation** - `total += num` adds to running sum
- **Loop exit** - Automatic when condition becomes false
- **Post-loop output** - After loop ends, display the result

## 💡 What I Learned

Building this project reinforced:
- **Loop patterns** - Understanding accumulation and conditional loops
- **Input handling** - Getting user input and converting to integers
- **Running calculations** - Maintaining state across iterations
- **Control flow** - How conditions control program execution
- **User interaction** - Creating simple but effective user interfaces


## 📊 Common Scenarios

| Input Sequence | Result | Notes |
|---|---|---|
| 500, 500 | 1000 | Exactly reaches target |
| 600, 500 | 1100 | Exceeds target |
| 999, 1 | 1000 | Just reaches target |
| 100 (10 times) | 1000 | Many small numbers |
| 1001 | 1001 | Single number exceeds target |



## 📖 Code Quality

**Strengths:**
- ✅ Simple and straightforward logic
- ✅ Clear variable naming
- ✅ Proper loop termination condition
- ✅ User-friendly output message
- ✅ Correct main guard for reusability

**Potential Improvements:**
- Could add comments explaining the loop logic
- Could display progress feedback (e.g., "Current sum: 500")
- Could add input validation for non-integer values
- Could allow user to choose the target value

## 🎓 Learning Concepts Demonstrated

- **While loops** - Loop continues based on condition
- **Accumulation pattern** - Common pattern in programming
- **Variable state** - Maintaining and updating values
- **Input/Output** - Getting data from user and displaying results
- **Conditional logic** - Decision making based on values

## 📚 Real-World Applications

This pattern is used in:
- **Data collection** - Gathering info until complete
- **Game development** - Collecting points until winning condition
- **Financial systems** - Tracking totals until threshold
- **Quality control** - Accumulating samples until statistically valid
- **Monitoring systems** - Collecting metrics until alert threshold

## 🤝 Contributing

Feel free to suggest improvements or variations:
- Different target thresholds
- Enhanced user feedback
- Input validation
- Algorithmic optimizations

## 📄 License

This project is open source under the MIT License.

## 👤 Author

**Ledio Durmishaj**
- GitHub: [@Miami05](https://github.com/Miami05)
- Email: lediodurmishaj16@gmail.com

---


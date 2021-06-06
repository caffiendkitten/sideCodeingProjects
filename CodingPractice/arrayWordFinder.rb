# A simple program to check if a word is in an array.

array = ["hand","feet", "knee", "table"]

def swap_elements(array)
  array.each do |word|
    if word == "feet"
       puts "feet"
      else
     word.concat('s')  
    end
  end
end

swap_elements(array)
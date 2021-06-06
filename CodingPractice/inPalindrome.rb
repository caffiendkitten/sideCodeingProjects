# Simple Ruby Program to test if input is Palindrone

def is_palindrome?(string)
  # string == string.reverse
  count = 0
  split_str = string.split('')

  split_str.each do |char|
    while count < string.length do
      count += 1

    end
  end
end


is_palindrome?("taocat")

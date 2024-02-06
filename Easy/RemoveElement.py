#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:51:46 2024

@author: kiran
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums :
            return 0
        
        if len(nums) == 1 :
            if nums[0] == val :
                return 0
            else : 
                return 1
        
        startPoint = 0
        endPoint = len(nums) -1
        counter = 0

        while startPoint <= endPoint :
            
            print("in while loop")

            #check if start and end are the same and add to counter
            if startPoint == endPoint :
                print("start = end")
                if nums[startPoint] == val :
                    counter += 1
                break

            if nums[startPoint] == val :
                print("startPoint is val")
                if nums[endPoint] != val :
                    print("startPoint is val and endPoint is not val")
                    nums[startPoint] = nums[endPoint]
                    startPoint += 1
                    endPoint -= 1
                    counter += 1

                if nums[endPoint] == val :
                    print("startPoint is val and endPoint is val")
                    counter += 1
                    endPoint -= 1
            
            else :
                print("startPoint is not val")
                startPoint += 1

        return len(nums) - counter
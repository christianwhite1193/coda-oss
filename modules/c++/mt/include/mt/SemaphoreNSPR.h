/* =========================================================================
 * This file is part of mt-c++ 
 * =========================================================================
 * 
 * (C) Copyright 2004 - 2009, General Dynamics - Advanced Information Systems
 *
 * mt-c++ is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program; If not, 
 * see <http://www.gnu.org/licenses/>.
 *
 */


#ifndef __MT_SEMAPHORE_NSPR_H__
#define __MT_SEMAPHORE_NSPR_H__

#if defined(USE_NSPR_THREADS)

#include <except/Exception.h>

#include <mt/SemaphoreInterface.h>
#include <semaphore.h>

namespace mt
{
class SemaphoreNSPR : public SemaphoreInterface
{
public:
    SemaphoreNSPR(unsigned count = 0)
    {
        throw except::Exception("NSPR Does not use semaphores.");
    }
    ~SemaphoreNSPR()
    {}

    void wait()
    {}
    
    void signal()
    {}

};
}

#endif
#endif
